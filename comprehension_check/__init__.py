from otree.api import *



doc = """
Welcome page for subjects taking part to the designing of statistical communication plan
"""


class C(BaseConstants):
    NAME_IN_URL = 'comprehension_check'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice1 = models.BooleanField(blank=True)
    choice2 = models.BooleanField(blank=True)
    choice3 = models.BooleanField(blank=True)
    pass


# FUNCTIONS
# PAGES
class Questions(Page):
    pass

class Answers(Page):
    pass

class Transition(Page):
    pass



page_sequence = [Questions, Answers, Transition]
