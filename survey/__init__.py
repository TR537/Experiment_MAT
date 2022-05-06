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
    # about 3t of CO2e per capita in the US per year for heating, cooling, and powering households

    # Public Goods and Climate Change
    climate_wtp_gas = models.FloatField(
        label='''The average gas price in 2021 in the US was $3.01 per gallon.
                 How many cents of an increase in gas price would you be willing to pay as part of a carbon tax system?
                 For your information: the reduction in carbon emissions from a tax of 3 cents would offset enough carbon
                 to save about 80 football fields of arctic ice from melting during summer.
                 Please enter an integer to indicate the amount of cents you would be willing to pay on top of the $3.01:''',
                 # 1. Demand effect of price increase of gasoline [p.e.d. around -0.3 according to Coglianese2016]
                 # 2. CO2 emissions per liter of gasoline [2.323kg of CO2 per liter of combusted gasoline according to Andersson2019]
                 # 3. Annual gasoline consumption in liters [134.83 billion gallons = 5.10387071 × 10^11 liters per year in 2021 according to https://www.eia.gov/tools/faqs/faq.php?id=23&t=10]
                 # 4. Annual CO2 emissions from gasoline: 11.8562916593 x 10^5 t of CO2
                 # 5. increase of 3 cents (1%) decreases CO2 emissions by 118.562916593 x 10^3 t of CO2
                 # 6. 118,000 t of CO2 are equivalent to heating, cooling, and powering 40,000 people for a full year
                 # 
                 # a. 3 sqm of ice for every 1 t of CO2 [according to Notz2016]
                 # b. based on 4. this makes 355.688749779 x 10^3 sqm of ice disappear (in summer)
                 # c. a football field is 4'462.272 sqm (excluding end zones)
                 # d. therefore, this takes away 79.7102350056 football fields
        min=0,
    )
    climate_wtp_tax = models.FloatField(
        label='''The Paris Climate Agreement has set a goal of not going above 1.5 degree centigrade temperature increase globally
                 compared to pre-industrial levels.
                 For your information: Should we fail to reach that goal, it would cost about $670 per person per year in the US alone to fight climate change.
                 How much of your current household income would you be willing to pay as part of a carbon tax to finance research
                 that could definitely prevent going above 1.5 degree centigrades?
                 Please enter a percentage between 0 and 100:''',
                 # 2 billion $ in the US alone
        min=0,
        max=100,
    )
    climate_wtp_flight = models.FloatField(
        label='''On average, flying 100 miles (domestically) cost about $50 in 2020.
                 How much would you be willing to pay on top of the usual price of a plane ticket as part of a carbon tax system?
                 This tax would be raised on every flight, not just the ones you book.
                 For your information: the reduction in carbon emissions from a tax of $1.00 would offset enough carbon
                 to save about 1,000 football fields of arctic ice from melting during summer.
                 Please enter how many dollars you would be willing to pay on top of the $50 per 100 miles (you are allowed to use decimals):''',
                 # [according to Hofer2010 2% ($1) tax would reduce carbon in US alone by 1.5 million tons of CO2]
                 # 1.5 million tons = heating, cooling, and powering half a million people in the US for a year [according to Goldstein2020]
                 #
                 # a. 4.5 million sqm ice saved
                 # b. therefore, this takes away 1'008.4548857622 football fields
        min=0,
    )
    # Not Public Goods
    pol_socialsec_wtp = models.FloatField(
        label='''The social security administration provides pensions to retired workers using the taxes you are currently paying.
                 Right now the average pension (through the social security administration) is $15,000 per retiree per year.
                 How much of your current household income would you be willing to pay to increase social security benefits
                 by $1,500 per retiree per year (a 10% increase)?
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
                 [2, '''In the game you played repeatedly with other people.
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
    items = ['climate_wtp_gas', 'climate_wtp_tax', 'climate_wtp_flight',  # WTP climate
             'pol_socialsec_wtp', 'pol_poor_wtp', 'pol_agriculture_wtp',  # WTP other policies
             'att_check3',  # checking if participant is paying attention
             ]
    random.shuffle(items)  # shuffling into random order
    items = items + ['inf_ret1', 'inf_ret2', 'hyp']
    form_fields = items


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'residence', 'education', 'pol_interest', 'pol_party']


class PaymentInfo(Page):
    pass


page_sequence = [Survey, Demographics]
