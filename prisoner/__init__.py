from otree.api import *


doc = """
This is a repeated PD game
"""


class C(BaseConstants):
    NAME_IN_URL = 'decision_1'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    INSTRUCTIONS_TEMPLATE = 'introduction/instructions.html'
    z = 150 # initial endowment
    r = 0.1 # interest on investing
    # Payoffs for all actions
    payoff_Idef = cu(z + 0.5 * (1 + r) * z) # A
    payoff_both_coop = cu((1 + r) * z) # B
    payoff_both_defect = cu(z) # C
    payoff_Icoop = cu(0.5 * (1 + r) * z) # D
    # minimum delta formulas
    delta_min = (1-r)/(1+r)
    delta_risk_dom_min = 1-r

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    treatment = models.BooleanField()


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
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        # save each participant's current group ID so it can be
        # accessed in the next app.
        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id
            if (participant.past_group_id % 2) ==0:
                participant.treatment = True
            else:
                participant.treatment = False

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['cooperate']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        session = player.session

        if participant.is_dropout:
            return 1  # instant timeout, 1 seconds
        else:
            return session.min_time

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant

        if timeout_happened:
            player.cooperate = False
            participant.is_dropout = True


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

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant
        session = player.session

        if participant.is_dropout:
            return 1  # instant timeout, 1 seconds
        else:
            return session.min_time

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant

        if timeout_happened:
            participant.is_dropout = True


page_sequence = [GroupingWaitPage, Decision, ResultsWaitPage, Results]
