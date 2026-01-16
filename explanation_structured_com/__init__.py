from otree.api import *



doc = """
Welcome page for subjects taking part to the designing of statistical communication plan
"""


class C(BaseConstants):
    NAME_IN_URL = 'explanation_structured_com'
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
class Explanation1(Page):
    pass

class Explanation2(Page):
    pass

# class Explanation3(Page):
#     pass


page_sequence = [Explanation1, Explanation2] #,Explanation3
