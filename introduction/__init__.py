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

    # Setting Strikes and Dropouts to false for all participants
    for p in subsession.get_players():
        p.participant.strike = False
        p.participant.is_dropout = False

    # Continuation probability from 6th round on
    session.cont_prob_percent = 75
    # Maximum time for making a decision
    session.min_time = 60
    # Bonus for answering all questions correctly
    inf_bonus = cu(500)
    ### Store Bonus in session variable
    session.inf_bonus = {
        'first_try': inf_bonus,
        'second_try': inf_bonus/2,
    }

    # Parameters for Payoffs
    session.z = 200  # initial endowment
    session.r = 0.2  # interest on investing
    session.r_percent = int(session.r * 100)
    session.t = int(0.5 * session.z) # tax for treatment game

    # Payoffs
    session.payoff_matrix = {
        'both_coop': cu((1 + session.r) * session.z),  # B
        'both_defect': cu(session.z),  # C
        'I_def': cu(session.z + 0.5 * (1 + session.r) * session.z),  # A
        'I_def_t': cu(session.z + 0.5 * (1 + session.r) * session.z - session.t), # A but with tax
        'I_coop': cu(0.5 * (1 + session.r) * session.z),  # D
        'I_coop_t': cu(0.5 * (1 + session.r) * session.z + session.t),  # D but with tax
    }

    # Labels for Buttons in the game
    session.strat_labels = {
        'cooperate': 'invest',
        'defect': 'not invest',
    }

    # Discount Factor border values
    session.delta_min = (1 - session.r) / (1 + session.r)
    session.delta_risk_dom_min = 1 - session.r

# PAGES
class Introduction(Page):
    pass

page_sequence = [Introduction]
