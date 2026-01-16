from otree.api import *
import time


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
    start_time = models.FloatField()
    time_spent = models.FloatField()
    private_account_balance_p1 = models.IntegerField(
        choices=[
            [4, '4 tokens'],
            [6, '6 tokens']
        ],
        label="How many tokens are there in participant 1’s private account?",
        widget=widgets.RadioSelect
    )
    check_total_contribution = models.IntegerField(
        choices=[
            [6, '6 tokens'],
            [10, '10 tokens']
        ],
        label="How many tokens are there in the shared account?",
        widget=widgets.RadioSelect
    )
    check_tokens_from_common_project = models.IntegerField(
        choices=[
            [2, '2 tokens'],
            [6, '6 tokens']
        ],
        label="How many tokens does the shared account return to each participant?",
        widget=widgets.RadioSelect
    )
    best_strategy_gamma_high = models.StringField(
        choices=["Invest all tokens in shared account",
                 "Keep all tokens in private account",
                 "Invest half of tokens in the shared account",
                 "It depends on Player 2 's strategy"],
        label="What is the best allocation decision of Player 1's to maximize their payment?",
        widget=widgets.RadioSelect
    )

# FUNCTIONS



# PAGES
class Questions(Page):
    form_model = 'player'
    form_fields = ["private_account_balance_p1",
                   "check_total_contribution", "check_tokens_from_common_project", "best_strategy_gamma_high"]

    @staticmethod
    def vars_for_template(player: Player):
        if player.field_maybe_none('start_time') is None:
            player.start_time = time.time()

    def error_message(self, values):
        solutions = dict(
            private_account_balance_p1=4,
            check_total_contribution=10,
            check_tokens_from_common_project=6,
            best_strategy_gamma_high="Invest all tokens in shared account"
        )
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                return 'Wrong answer. Please try again.' #By default, otree treat any return text from a function as an error on htlm page
            else:
                pass

    @staticmethod
    def before_next_page(player: Player, timeout_happened=False):
        player.time_spent = time.time() - player.start_time


class Transition(Page):
    pass


page_sequence = [Questions, Transition]
