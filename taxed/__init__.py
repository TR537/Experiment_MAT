from otree.api import *


doc = """
This is the PD game with a tax for not cooperating.
"""


class C(BaseConstants):
    NAME_IN_URL = 'decision_2'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 30
    INSTRUCTIONS_TEMPLATE = 'introduction/instructions.html'
    INSTRUCTIONS_TEMPLATE_T = 'introduction/instructions_t.html'

    # Treatments
    TREATMENTS = [True, False]

class Subsession(BaseSubsession):
    num_groups_created = models.IntegerField(initial=0)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'A'], [False, 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p, group)

def other_player(player: Player):
    return player.get_others_in_group()[0]

def set_payoff(player: Player, group: Group):
    session = player.session
    payoff_matrix_cont = {
        (False, True): session.payoff_matrix['I_def'],
        (True, True): session.payoff_matrix['both_coop'],
        (False, False): session.payoff_matrix['both_defect'],
        (True, False): session.payoff_matrix['I_coop'],
    }
    payoff_matrix_treat = {
        (False, True): session.payoff_matrix['I_def_t'],
        (True, True): session.payoff_matrix['both_coop'],
        (False, False): session.payoff_matrix['both_defect'],
        (True, False): session.payoff_matrix['I_coop_t'],
    }
    other = other_player(player)
    if player.participant.treatment:
        player.payoff = payoff_matrix_treat[(player.cooperate, other.cooperate)]
    else:
        player.payoff = payoff_matrix_cont[(player.cooperate, other.cooperate)]

def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    # we now place users into different baskets, according to their group in the previous app.
    # the dict 'd' will contain all these baskets.
    d = {}
    for p in waiting_players:
        group_id = p.participant.past_group_id
        if group_id not in d:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            d[group_id] = []
        players_in_my_group = d[group_id]
        players_in_my_group.append(p)
        if len(players_in_my_group) == 2:
            return players_in_my_group
        # print('d is', d)

# PAGES
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def after_all_players_arrive(group: Group):
        subsession = group.subsession

        # % is the modulus operator.
        # so when num_groups_created exceeds the max list index,
        # we go back to 0, thus creating a cycle.
        idx = subsession.num_groups_created % len(C.TREATMENTS)

        treatment = C.TREATMENTS[idx]

        for p in group.get_players():
            # since we want the treatment to persist for all rounds, we need to assign it
            # in a participant field (which persists across rounds)
            # rather than a group field, which is specific to the round.
            p.participant.treatment = treatment
            # For finishing at a random point
            p.participant.finished_rounds = False

        subsession.num_groups_created += 1

class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if participant.is_dropout:
            return 0.1  # instant timeout, 0.1 seconds
        else:
            return 60

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
            if participant.treatment:
                player.cooperate = True
            else:
                player.cooperate = False
            if participant.strike:
                participant.is_dropout = True
            else:
                participant.strike = True


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        import random
        if random.random() > (group.session.cont_prob_percent / 100):
            for p in group.get_players():
                p.participant.finished_rounds = True
        set_payoffs(group)

class Results(Page):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        participant = player.participant
        if participant.finished_rounds:
            return upcoming_apps[0]
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
            return 0.1  # instant timeout, 1 seconds
        else:
            return session.min_time
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant

        if timeout_happened:
            if participant.strike:
                participant.is_dropout = True
            else:
                participant.strike = True


page_sequence = [GroupingWaitPage, Introduction, Decision, ResultsWaitPage, Results]
