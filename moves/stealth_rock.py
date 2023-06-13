from .move import Move
from waifu_types.type import Type

class StealthRock(Move):
    def __init__(self):
        super().__init__("Stealth Rock", type=Type.ROCK, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Damages opponent switching into battle.
        """
        pass
