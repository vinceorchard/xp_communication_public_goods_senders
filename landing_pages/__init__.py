from otree.api import *



doc = """
Welcome page for subjects taking part to the designing of statistical communication plan
"""


class C(BaseConstants):
    NAME_IN_URL = 'welcome_page'
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
class WelcomePage(Page):
    pass


class EthicDataPage(Page):
    pass


class ConsentPage(Page):
    pass



page_sequence = [WelcomePage,EthicDataPage,ConsentPage]
