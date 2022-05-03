from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ##################################################################
    ####################### FloatFields ##############################
    ##################################################################
    # Public Goods and Climate Change
    climate_wtp_gas = models.FloatField(
        label='''The average gas price in 2021 in the US was $3.01 per gallon.
                 How many cents of an increase in gas price would you be willing to pay as part of a carbon tax system?
                 Please enter an integer to indicate the amount of cents you would be willing to pay on top of the $3.01:''',
                 # e.g. increase by 2 cents would reduce emissions from private transportation by x percent
                 # e.g. 1 kg co2 = 1 m^2 rain forest to desert
                 # 1. Demand effect of price increase of gasoline 
                 # 2. CO2 emissions per liter of gasoline 
                 # 3. 1. x 2. = reduction in CO2 emissions from tax 
                 # 4. convert 3. in easy to understand environmental damages
        min=0,
    )
    climate_wtp_tax = models.FloatField(
        label='''Reaching the Paris Climate Agreement goal of not going above 1.5 degree centigrade temperature increase globally
                 would save about $2 billion per year in the US alone compared to not doing anything against climate change.
                 How much of your current household income would you be willing to pay as part of a carbon tax to finance research
                 that could mitigate further temperature increase?
                 Please enter a percentage between 0 and 100:''',
                 # 1. saved CO2 emissions if we don't go above 1.5 C compared to projection
                 # 2. cost of reaching that goal compared to not doing anything
        min=0,
        max=100,
    )
    climate_wtp_flight = models.FloatField(
        label='''On average, flying 100 miles (domestically) cost about $50 in 2020.
                 How much would you be willing to pay on top of the usual price of a plane ticket as part of a carbon tax system?
                 Please enter how many dollars you would be willing to pay on top of the $50 per 100 miles (does not need to be a whole number):''',
                 # 1. demand effect of flying
                 # 2. CO2 emissions per mile flown in the US
                 # 3. 1. x 2. = reduction in CO2 emissions from tax
                 # 4. convert 3. in easy to understand environmental damages
        min=0,
    )
    climate_wtp_energy = models.FloatField(
        label='''Installing an average solar system network on a residential house in the US costs about $10,000.
                 How much of your current household income would you be willing to pay as part of a carbon tax to finance
                 an average government refund of $2,000 per solar system (a 20% subsidy)?
                 Please enter a percentage between 0 and 100:''',
                 # maybe leave this one out.
        min=0,
        max=100,
    )
    # Not Public Goods
    pol_socialsec_wtp = models.FloatField(
        label='''The social security administration provides pensions to retired workers using the taxes you are currently paying.
                 Right now the average pension (through the social security administration) is $15,000 per retiree per year.
                 How much of your current household income would you be willing to pay to increase social security benefits
                 by $1,500 per person per year (a 10% increase)?
                 Please enter a percentage between 0 and 100:''',
        min=0,
        max=100,
    )
    pol_poor_wtp = models.FloatField(
        label='''In 2018 the US spent approximately $11,000 on social benefits per person.
                 These benefits are primarily given to low-income households to subsidize their cost of living.  
                 How much of your current household income would you be willing to pay to increase
                 average social benefits by $1,000 (an increase of roughly 10%)?
                 Please enter a percentage between 0 and 100:''',
        min=0,
        max=100,
    )
    pol_agriculture_wtp = models.FloatField(
        label='''In 2020 the US spent approximately $10 billion on subsidies for farmers in the US.
                 These benefits are primarily used to grow crops like corn, soy, and wheat, which are used in processed foods.  
                 How much of your current household income would you be willing to pay to increase
                 this subsidy towards the US agriculture industry by $1 billion (an increase of roughly 10%)?
                 Please enter a percentage between 0 and 100:''',
        min=0,
        max=100,
    )
    ##################################################################
    ###################### Hypothesis Checks #########################
    ##################################################################
    hyp = models.StringField(
        label='State in one sentence: What do you believe the current study is about?',
        widget=widgets.TextArea
    )
    ##################################################################
    ####################### Attention Checks #########################
    ##################################################################
    att_check1 = models.BooleanField(
        choices=[[False, "1 - Strongly Democrat"],
                 [True, "2 - Democrat"],
                 [False, "3 - Independent, lean Democrat"],
                 [False, "4 - Independent"],
                 [False, "5 - Independent, lean Republican"],
                 [False, "6 - Republican"],
                 [False, "7 - Strongly Republican"],
                 ],
        label='We are using this question to check your attention. Please select “Democrat”.',
        widget=widgets.RadioSelect,
    )
    att_check2 = models.BooleanField(
        choices=[[False, "1 - Strongly Democrat"],
                 [False, "2 - Democrat"],
                 [False, "3 - Independent, lean Democrat"],
                 [False, "4 - Independent"],
                 [False, "5 - Independent, lean Republican"],
                 [True, "6 - Republican"],
                 [False, "7 - Strongly Republican"],
                 ],
        label='We are using this question to check your attention. Please select “Republican”.',
        widget=widgets.RadioSelect,
    )
    att_check3 = models.FloatField(
        label='We are using this question to check your attention. Please enter 2022.',
    )
    ##################################################################
    ################## Socio-economic information ####################
    ##################################################################
    age = models.IntegerField(label='What is your age?', min=13, max=120)
    gender = models.StringField(
        choices=[['Male', 'Male'],
                 ['Female', 'Female'],
                 ['other', 'other'],
                 ],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    residence = models.StringField(
        choices=[['US', 'US'],
                 ['Canada', 'Canada'],
                 ['other', 'other'],
                 ],
        label='Where do you currently live?',
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        choices=[['Primary School', 'Primary School'],
                 ['High School', 'High School'],
                 ['Bachelors Degree', 'Bachelors Degree'],
                 ['Masters Degree', 'Masters Degree'],
                 ['PhD', 'PhD'],
                 ],
        label='What is the highest degree of education that you have obtained?',
        widget=widgets.RadioSelect,
    )
    pol_interest = models.IntegerField(
        choices=[[1, "1 - Very uninterested"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Very interested"]
                 ],
        label='How interested are you in politics?',
        widget=widgets.RadioSelect,
    )
    pol_party = models.IntegerField(
        choices=[[1, "1 - Strongly liberal"],
                 [2, "2 - Liberal"],
                 [3, "3 - Slightly liberal"],
                 [4, "4 - Moderate, middle of the road"],
                 [5, "5 - Slightly conservative"],
                 [6, "6 - Conservative"],
                 [7, "7 - Strongly conservative"],
                 ],
        label='When it comes to politics, do you think of yourself as a liberal, conservative, or moderate?',
        widget=widgets.RadioSelect,
    )
    ##################################################################
    ############### Check for information retention ##################
    ##################################################################
    inf_ret1 = models.IntegerField(
        label='''You just played a game.
                 Please try to remember the game and select the statement that best describes what happened in the game.''',
        choices=[[1, '''In the game you were given 200 points every round and if you invested the points,
                        there was a fifty fifty chance that the points would increase or decrease.'''],
                 [2, '''In the game you played repeatedly with another person.
                        If neither invested, then everybody kept their initial amount of points.
                        If both invested, this gave both of you a higher payoff.
                        If only one person invested, then this person got less points, while the not investing person got more points.'''],
                 # Correct
                 [3, '''In the game you could choose between 2 strategies 
                        and only your choice mattered for the determination of the points you received.
                        This is typical for public goods, where your action alone is determining the provision of a good.'''],
                 ],
        widget=widgets.RadioSelect,
    )
    inf_ret2 = models.IntegerField(
        label='''In the beginning you got information about public goods.
                 Please choose which of the following is a public good.''',
        choices=[[1, 'Happy Meal from McDonald\'s'],
                 [2, 'Cable TV'],
                 [3, 'National Defense'],  # Correct
                 ],
        widget=widgets.RadioSelect,
    )


# FUNCTIONS

# PAGES
class Survey(Page):
    form_model = 'player'
    items = ['climate_wtp_gas', 'climate_wtp_tax', 'climate_wtp_flight', 'climate_wtp_energy',  # WTP climate
             'pol_socialsec_wtp', 'pol_poor_wtp', 'pol_agriculture_wtp',  # WTP other policies
             'att_check3',  # checking if participant is paying attention
             ]
    random.shuffle(items)  # shuffling into random order
    items = items + ['inf_ret1', 'inf_ret2']
    form_fields = items


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'residence', 'education', 'pol_interest', 'pol_party']


class PaymentInfo(Page):
    pass


page_sequence = [Survey, Demographics]
