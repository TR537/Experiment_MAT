from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'information'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    WAIT_TIME = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Timer value
    page_pass_time = models.FloatField()
    # Information Provision
    inf_prov1 = models.IntegerField(
        label='Question 1: What is the major problem in the provision of public goods?',
        choices=[[1, "People tend to pay too much for public goods. It becomes hard to redistribute the excess funding."],
                 [2, "People can profit from other people's investment without investing themselves."], #correct
                 [3, "It is hard to distribute the public good to everybody."]
                 ],
        widget=widgets.RadioSelect,
    )
    inf_prov2 = models.IntegerField(
        label='Question 2: Which of the following constitutes a public good?',
        choices=[[1, "Cell Phone Service"],
                 [2, "Environmental Policies"], # Correct
                 [3, "Cars"]
                 ],
        widget=widgets.RadioSelect,
    )
    inf_prov3 = models.IntegerField(
        label='Question 3: How can governments improve public good provision in real-world applications?',
        choices=[[1, "Taxing people who are not willing to contribute."], # correct
                 [2, '''In the real world it is not possible to increase public good contributions.
                        Private organization would make more sense anyways since it is more efficient.'''],
                 [3, '''Not doing anything, since free markets balance themselves.
                        Therefore, any level of public good is actually optimal if it is determined by the free market.''']
                 ],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
def set_payoff(player: Player):
    session = player.session
    if (player.inf_prov1 == 2) and (player.inf_prov2 == 2) and (player.inf_prov3 == 1):
        if player.round_number == 1:
            player.payoff = session.inf_bonus['first_try']
        elif player.round_number == 2:
            player.payoff = session.inf_bonus['second_try']
        elif player.round_number == 3:
            player.payoff = session.inf_bonus['third_try']
    else:
        player.payoff = 0

# PAGES
class InformationIntervention(Page):
    form_model = 'player'
    form_fields = ['inf_prov1', 'inf_prov2', 'inf_prov3']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_pass_time = time.time() + C.WAIT_TIME
        set_payoff(player)
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        return dict(
            inf_bonus={
                'first_try': session.inf_bonus['first_try'].to_real_world_currency(session),
                'second_try': session.inf_bonus['second_try'].to_real_world_currency(session),
                'third_try': session.inf_bonus['third_try'].to_real_world_currency(session),
            }
        )


class InformationEvaluation(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        first_try, second_try, third_try = False, False, False
        if player.payoff == session.inf_bonus['first_try']:
            first_try = True
        elif player.payoff == session.inf_bonus['second_try']:
            second_try = True
        elif player.payoff == session.inf_bonus['third_try']:
            third_try = True
        return dict(
            first_try=first_try,
            second_try=second_try,
            third_try=third_try,
            inf_prov1=player.inf_prov1,
            inf_prov2=player.inf_prov2,
            inf_prov3=player.inf_prov3,
            explanation1={1: '''The first answer is wrong because people tend to underprovide a public good.''',
                          2: '''The second statement is correct since this is the free-riding problem
                                that was discussed in the text. I.e. people get a benefit from
                                other people investing regardless of their own contribution.''',
                          3: '''The third answer is wrong because a public good is generally automatically consumed
                                (e.g. public defence is always consumed by any resident).''',
                          },
            explanation2={1: '''The first answer is wrong because cell phone service is generally privately organized.
                                You pay for the messages you send, the calls you make and the data you use
                                and not for anybody else's use of the service.''',
                          2: '''Environmental Policies are useful to everybody that would be affected
                                from the consequences of not having them in place. For example, if there was a world-wide subsidy
                                to use green energy, everybody would profit from less green-house-gas emissions.
                                Therefore, the second statement is correct.''',
                          3: '''The third statement is wrong since cars can be privately owned and they only provide use
                                to the owner.''',
                          },
            explanation3={1: '''The first statement is correct.
                                Taxation is currently the best option to make people provide public goods.''',
                          2: '''The second answer is wrong. While private organization works well for many goods,
                                it is not the best way to improve public good provision.
                                Public goods cannot be sold in the conventional sense and therefore,
                                a private company will have a hard time turning a profit from providing a public good.''',
                          3: '''The third answer is wrong since even the more conservative anti-tax economists agree
                                that in the case of public goods, the free market fails. A tax corrects for that market failure.''',
                          },
            payoff=player.payoff.to_real_world_currency(session),
        )
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if (player.inf_prov1 == 2) and (player.inf_prov2 == 2) and (player.inf_prov3 == 1):
            return upcoming_apps[0]

page_sequence = [InformationIntervention, InformationEvaluation]
