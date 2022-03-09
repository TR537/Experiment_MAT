from os import environ


SESSION_CONFIGS = [
    dict(
        name='all_in_one',
        display_name="All in one",
        app_sequence=['introduction', 'prisoner', 'taxed', 'survey', 'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='prisoner',
        display_name="Prisoner Game",
        app_sequence=['prisoner'],
        num_demo_participants=2,
    ),
    dict(
        name='taxed',
        display_name="Taxed Game",
        app_sequence=['taxed'],
        num_demo_participants=4,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=2
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
        mturk_hit_settings=dict(
            keywords='bonus, study',
            title='Title for your experiment',
            description='Description for your experiment',
            frame_height=500,
            template='global/mturk_template.html',
            minutes_allotted_per_assignment=60,
            expiration_hours=7 * 24,
            qualification_requirements=[]
            # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
),
)

PARTICIPANT_FIELDS = ['treatment']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '4143000320156'

INSTALLED_APPS = ['otree', 'otreeutils']
