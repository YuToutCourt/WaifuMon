from ..move import Move
from waifu_types.type import Type

class SpicyExtract(Move):
    def __init__(self):
        super().__init__("Spicy Extract", type=Type.GRASS, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Harshly lowers the opponent's Defense and sharply raises their Attack.
        """
        pass
