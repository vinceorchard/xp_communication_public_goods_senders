from otree.api import *
import numpy as np
from random import sample


class C(BaseConstants):
    NAME_IN_URL = 'communication_structured_com'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    ARRAY_MULTIPLIER = sample([0.6, 0.9], k=2)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    multiplier_value = models.FloatField()
    stat_message_sent = models.StringField(choices = ["The value of \( \gamma \) is 0.6", "The value of \( \gamma \) is 0.9"],
                                            label = "Which message do you want to send to the two players?",
                                           widget=widgets.RadioSelectHorizontal)
    # message_high = models.IntegerField(max=100, min=0, label="The factor is high")
    # message_low = models.IntegerField(max=100, min=0, label="The factor is low")
    # message_none = models.IntegerField(max=100, min=0, label="No Message")


# def validate_messages(player: Player):
#     total = player.message_high + player.message_low + player.message_none
#     if total != 100:
#         return 'The probabilities must sum to 100%'
#     else:
#         pass

# FUNCTIONS
# PAGES

class ChooseMessage_statistic(Page):
    form_model = 'player'
    form_fields = ['stat_message_sent']
    @staticmethod
    def vars_for_template(player: Player):
        player.multiplier_value = C.ARRAY_MULTIPLIER[player.round_number-1]

#
# class Demographics(Page):
#     form_model = 'player'
#     form_fields = ['age', 'gender']


page_sequence = [ChooseMessage_statistic]


