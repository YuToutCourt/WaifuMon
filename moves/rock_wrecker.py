from .move import Move
from waifu_types.type import Type

class RockWrecker(Move):
    def __init__(self):
        super().__init__("Rock Wrecker", type=Type.ROCK, power=150, accuracy=90, pp=5, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass
