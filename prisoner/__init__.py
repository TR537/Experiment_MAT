from otree.api import *


doc = """
This is a repeated PD game
"""


class C(BaseConstants):
    NAME_IN_URL = 'prisoner'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    INSTRUCTIONS_TEMPLATE = 'prisoner/instructions.html'
    z = 100 # initial endowment
    r = 0.2 # interest on investing
    payoff_Idef = cu(z + 0.5 * (1 + r) * z) # A
    payoff_both_coop = cu((1 + r) * z) # B
    payoff_both_defect = cu(z) # C
    payoff_Icoop = cu(0.5 * (1 + r) * z) # D

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'A'], [False, 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)

def other_player(player: Player):
    return player.get_others_in_group()[0]


def set_payoff(player: Player):
    payoff_matrix = {
        (False, True): C.payoff_Idef,
        (True, True): C.payoff_both_coop,
        (False, False): C.payoff_both_defect,
        (True, False): C.payoff_Icoop,
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


page_sequence = [Decision, ResultsWaitPage, Results]
