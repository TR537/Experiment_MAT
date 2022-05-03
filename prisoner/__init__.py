from otree.api import *


doc = """
This is a repeated PD game
"""


class C(BaseConstants):
    NAME_IN_URL = 'decision_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    INSTRUCTIONS_TEMPLATE = 'introduction/instructions.html'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    treatment = models.BooleanField()


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'invest'], [False, 'not invest']],
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
    session = player.session
    payoff_matrix = {
        (False, True): session.payoff_matrix['I_def'],
        (True, True): session.payoff_matrix['both_coop'],
        (False, False): session.payoff_matrix['both_defect'],
        (True, False): session.payoff_matrix['I_coop'],
    }
    other = other_player(player)
    player.payoff = payoff_matrix[(player.cooperate, other.cooperate)]


# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = '''You might wait for a while on this waitpage until someone else joins the game.
                   Please don't get discouraged and don't leave the site. You should still not exceed the 30 minutes and you will be paid at least USD 3.00.'''

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



page_sequence = [GroupingWaitPage, Decision, ResultsWaitPage, Results]
