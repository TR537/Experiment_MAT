from otree.api import *


doc = """
This is the PD game with a tax for not cooperating.
"""


class C(BaseConstants):
    NAME_IN_URL = 'decision_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    INSTRUCTIONS_TEMPLATE = 'taxed/instructions.html'
    z = 120
    r = 0.2

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    treatment = models.BooleanField()
    payoff_both_coop = models.CurrencyField()
    payoff_both_defect = models.CurrencyField()
    payoff_Icoop = models.CurrencyField()
    payoff_Idef = models.CurrencyField()
    t = models.IntegerField(initial=0)

class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'A'], [False, 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
def creating_session(subsession):
    import itertools
    treatments = itertools.cycle([True, False])
    for group in subsession.get_groups():
        if subsession.round_number == 1:
            group.treatment = next(treatments)
            players = group.get_players()
            for p in players:
                p.participant.treatment = group.treatment
        else:
            group.treatment = group.in_round(1).treatment
        if group.treatment:
            group.t = int(0.5 * C.z)
        group.payoff_both_coop = cu((1 + C.r) * C.z)
        group.payoff_both_defect = cu(C.z)
        group.payoff_Icoop = cu(0.5 * (1 + C.r) * C.z + group.t)
        group.payoff_Idef = cu(C.z + 0.5 * (1 + C.r) * C.z - group.t)

def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p, group)

def other_player(player: Player):
    return player.get_others_in_group()[0]

def set_payoff(player: Player, group: Group):
    payoff_matrix = {
        (False, True): group.payoff_Idef,
        (True, True): group.payoff_both_coop,
        (False, False): group.payoff_both_defect,
        (True, False): group.payoff_Icoop,
    }
    other = other_player(player)
    player.payoff = payoff_matrix[(player.cooperate, other.cooperate)]

# PAGES
class Introduction(Page):
    timeout_seconds = 100


class Decision(Page):
    form_model = 'player'
    form_fields = ['cooperate']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        opponent = other_player(player)
        return dict(
            opponent=opponent,
            same_choice=player.cooperate == opponent.cooperate,
            my_decision=player.field_display('cooperate'),
            opponent_decision=opponent.field_display('cooperate'),
        )


page_sequence = [Introduction, Decision, ResultsWaitPage, Results]
