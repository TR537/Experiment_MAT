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
        choices=[['Primary School', 'Primary School'], ['High School', 'High School'], ['Bachelors Degree', 'Bachelors Degree'], ['Masters Degree', 'Masters Degree'], ['PhD', 'PhD']],
        label='What is the highest degree of education that you have obtained?',
        widget=widgets.RadioSelect,
    )
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
    hyp = models.StringField(
        label='''
        State in one sentence: What do you believe the current study is about?''',
        widget=widgets.TextArea
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'residence', 'education']


class PoliticalAttitude(Page):
    form_model = 'player'
    form_fields = ['pol_def']

class HypothesisQuestion(Page):
    form_model = 'player'
    form_fields = ['hyp']


page_sequence = [PoliticalAttitude, Demographics, HypothesisQuestion]
