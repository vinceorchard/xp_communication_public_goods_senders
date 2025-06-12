from otree.api import *



doc = """
Transition page from bot public good game to eliciting communication plans
"""


class C(BaseConstants):
    NAME_IN_URL = 'waiting_page_for_results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField(label ="")
    pass

# FUNCTIONS
# PAGES
class WaitingPageResults(Page):
    pass

class CollectID(Page):
    form_model = 'player'
    form_fields = ['prolific_id']


page_sequence = [CollectID, WaitingPageResults]

