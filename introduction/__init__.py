from otree.api import *


doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'introduction/instructions.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def creating_session(subsession):
    session = subsession.session
    session.cont_prob_percent = 85
    for p in subsession.get_players():
        p.participant.is_dropout = False

    session.payoff_Idef = cu(300)  # A
    session.payoff_both_coop = cu(200)  # B
    session.payoff_both_defect = cu(100)  # C
    session.payoff_Icoop = cu(0)  # D

    session.min_time = 30

# PAGES
class Introduction(Page):
    pass

page_sequence = [Introduction]
