from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Information Provision
    inf_prov1 = models.BooleanField(
        choices=[[False,
                  "There are usually too many funds and the excess money has to be redistributed which is a bureaucratic hassle."],
                 [True, "People can profit from other people's investment without investing themselves."],
                 [False, "It is hard to distribute the public good to everybody."]
                 ],
        label='What is the major problem in the provision of public goods?',
        widget=widgets.RadioSelect,
    )
    inf_prov2 = models.BooleanField(
        choices=[[False, "Healthcare"],
                 [True, "Environmental Policies"],
                 [False, "Cars"]
                 ],
        label='Which of the following constitute public goods?',
        widget=widgets.RadioSelect,
    )
    inf_prov3 = models.BooleanField(
        choices=[[True, "Taxing people who are not willing to contribute."],
                 [False, "Putting people in jail if they do not contribute."],
                 [False,
                  "Not doing anything, the market usually finds its equilibrium. Therefore, any level of provision is actually optimal already."]
                 ],
        label='How can public good provision be improved in real-world applications?',
        widget=widgets.RadioSelect,
    )
    # Political Attitude Survey
    pol_def = models.IntegerField(
        choices=[[1, "1 - Greatly decrease defense spending"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep defense spending about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase defense spending"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending on defense be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_def_wtp = models.IntegerField(
        label='How much of your current household income would you be willing to pay to increase defense budget? Please enter a percentage between 0 and 100:',
        min=0,
        max=100
    )
    pol_terror = models.IntegerField(
        choices=[[1, "1 - Greatly decrease war on terror spending"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep war on terror spending about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase war on terror spending"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending on the war on terrorism be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_terror_wtp = models.IntegerField(
        label='How much of your current household income would you be willing to pay to increase spending on the war on terrorism? Please enter a percentage between 0 and 100:',
        min=0,
        max=100
    )
    pol_poor = models.IntegerField(
        choices=[[1, "1 - Greatly decrease aid to the poor"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep aid to the poor about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase aid to the poor"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending on aid to the poor be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_health = models.IntegerField(
        choices=[[1, "1 - Greatly decrease healthcare spending"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep healthcare spending about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase healthcare spending"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending on healthcare be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_health_wtp = models.IntegerField(
        label='How much of your current household income would you be willing to pay towards universal healthcare in the US? Please enter a percentage between 0 and 100:',
        min=0,
        max=100
    )
    pol_blkaid = models.IntegerField(
        choices=[[1, "1 - Greatly decrease aid to blacks"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep aid to blacks about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase aid to blacks"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending to improve the social and economic position of blacks be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_adopt = models.IntegerField(
        choices=[[1, "1 - Favor strongly"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Neither favor nor oppose"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Oppose strongly"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Do you favor or oppose laws that prevent gay or lesbian couples from adopting children, or haven’t you thought much about it?',
        widget=widgets.RadioSelect,
    )
    pol_imm = models.IntegerField(
        choices=[[1, "1 - Greatly decrease spending on immigration control"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep spending on immigration control about the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Greatly increase spending on immigration control"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should federal spending to control immigration be increased, decreased, or kept the same?',
        widget=widgets.RadioSelect,
    )
    pol_guns = models.IntegerField(
        choices=[[1, "1 - Make it much more difficult"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Keep the rules the same"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Make it much easier"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Should the federal government make it more difficult for people to buy a gun than it is now, make it easier for people to buy a gun, or keep these rules about the same as they are now?',
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
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='When it comes to politics, do you think of yourself as a liberal, conservative, moderate, or haven’t you thought much about this?',
        widget=widgets.RadioSelect,
    )
    # Actually interesting items
    climate_gov = models.IntegerField(
        choices=[[1, "1 - Doing more about climate change"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4 - Doing the right amount"],
                 [5, "5"],
                 [6, "6"],
                 [7, "7 - Doing less about climate change"],
                 [8, "Don't know"],
                 [9, "I haven't thought much about it"]
                 ],
        label='Do you think the federal government should be doing more about climate change, should be doing less, or is it currently doing the right amount?',
        widget=widgets.RadioSelect,
    )
    climate_wtp_gas = models.IntegerField(
        label='The average gas price in 2021 in the US was USD 3.01 per gallon. How many cents of an increase in gas price would you be willing to pay as part of a carbon tax system? Please enter an integer to indicate the amount of cents you would be willing to pay on top of the USD 3.01:',
    )
    climate_wtp_tax = models.IntegerField(
        label='How much of your current household income would you be willing to pay to mitigate climate change outcomes? Please enter a percentage between 0 and 100:',
        min = 0,
        max = 100
    )
    # Hypothesis Check
    hyp = models.StringField(
        label='State in one sentence: What do you believe the current study is about?',
        widget=widgets.TextArea
    )
    # Attention Checks
    att_check1 = models.BooleanField(
        choices=[[False, "1 - Strongly Democrat"],
                 [False, "2 - Democrat"],
                 [False, "3 - Independent, lean Democrat"],
                 [False, "4 - Independent"],
                 [False, "5 - Independent, lean Republican"],
                 [False, "6 - Republican"],
                 [False, "7 - Strongly Republican"],
                 [True, "Don't know"],
                 [False, "I haven't thought much about it"]
                 ],
        label='We are using this question to check your attention. Please select “Don’t know”.',
        widget=widgets.RadioSelect,
    )
    att_check2 = models.BooleanField(
        choices=[[False, "1 - Strongly Democrat"],
                 [False, "2 - Democrat"],
                 [False, "3 - Independent, lean Democrat"],
                 [False, "4 - Independent"],
                 [False, "5 - Independent, lean Republican"],
                 [False, "6 - Republican"],
                 [False, "7 - Strongly Republican"],
                 [False, "Don't know"],
                 [True, "I haven't thought much about it"]
                 ],
        label='We are using this question to check your attention. Please select “I haven’t thought much about it”.',
        widget=widgets.RadioSelect,
    )
    # Standard Socio-Economic questions
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['other', 'other']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    residence = models.StringField(
        choices=[['US', 'US'], ['Canada', 'Canada'], ['other', 'other']],
        label='Where do you currently live?',
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        choices=[['Primary School', 'Primary School'], ['High School', 'High School'],
                 ['Bachelors Degree', 'Bachelors Degree'], ['Masters Degree', 'Masters Degree'], ['PhD', 'PhD']],
        label='What is the highest degree of education that you have obtained?',
        widget=widgets.RadioSelect,
    )



# FUNCTIONS
# PAGES

class InformationIntervention(Page):
    form_model = 'player'
    form_fields = ['inf_prov1', 'inf_prov2', 'inf_prov3']

class Survey(Page):
    form_model = 'player'
    form_fields = ['pol_def', 'pol_def_wtp', 'att_check1', 'climate_wtp_tax', 'pol_terror', 'pol_terror_wtp', 'pol_poor', 'climate_gov', 'pol_health', 'pol_health_wtp', 'pol_blkaid', 'att_check2', 'climate_wtp_gas', 'pol_adopt', 'pol_imm', 'pol_guns', 'pol_interest', 'pol_party', 'hyp']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'residence', 'education']

class InformationEvaluation(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            correct1=player.inf_prov1,
            correct2=player.inf_prov2,
            correct3=player.inf_prov3,
        )

page_sequence = [InformationIntervention, InformationEvaluation, Survey, Demographics]
