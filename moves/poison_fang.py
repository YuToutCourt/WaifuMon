from .move import Move
from waifu_types.type import Type

class PoisonFang(Move):
    def __init__(self):
        super().__init__("Poison Fang", type=Type.POISON, power=50, accuracy=100, pp=15, proba_effect=50)

    def effect(self):
        """
        May badly poison opponent.
        """
        pass
