from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        session = player.session
        return dict(redemption_code=participant.label or participant.code,
                    bonus=participant.payoff.to_real_world_currency(session),
                    fee=session.participation_fee,
                    total=participant.payoff_plus_participation_fee().to_real_world_currency(session)
                    )


page_sequence = [PaymentInfo]
