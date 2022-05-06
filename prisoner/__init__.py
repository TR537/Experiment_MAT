from otree.api import *
import random

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
    pass


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'invest'], [False, 'not invest']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    other_coop = models.BooleanField(initial=False)
    other_payoff = models.CurrencyField()


# FUNCTIONS
def set_payoff(player: Player):
    session = player.session
    payoff_matrix = {
        (False, True): session.payoff_matrix['I_def'],
        (True, True): session.payoff_matrix['both_coop'],
        (False, False): session.payoff_matrix['both_defect'],
        (True, False): session.payoff_matrix['I_coop'],
    }
    if random.random() < session.coop_prob[player.round_number-1]:
        player.other_coop = True

    player.payoff = payoff_matrix[(player.cooperate, player.other_coop)]
    player.other_payoff = payoff_matrix[(player.other_coop, player.cooperate)]
    # Add payoff to participant variable for payment
    if player.cooperate and not player.other_coop:
        player.participant.payment_other += cu(((1+session.r)*session.z)/2).to_real_world_currency(session)


# PAGES
class Decision(Page):
    form_model = 'player'
    form_fields = ['cooperate']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player)


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            same_choice=player.cooperate == player.other_coop,
            my_decision=player.cooperate,
            opponent_decision=player.other_coop,
        )


page_sequence = [Decision, Results]
