from .move import Move
from waifu_types.type import Type

class BuzzyBuzz(Move):
    def __init__(self):
        super().__init__("Buzzy Buzz", type=Type.ELECTRIC, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Paralyzes the opponent.
        """
        pass
