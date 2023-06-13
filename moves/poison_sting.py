from .move import Move
from waifu_types.type import Type

class PoisonSting(Move):
    def __init__(self):
        super().__init__("Poison Sting", type=Type.POISON, power=15, accuracy=100, pp=35, proba_effect=30)

    def effect(self):
        """
        May poison the opponent.
        """
        pass
