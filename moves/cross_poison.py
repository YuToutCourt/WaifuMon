from .move import Move
from waifu_types.type import Type

class CrossPoison(Move):
    def __init__(self):
        super().__init__("Cross Poison", type=Type.POISON, power=70, accuracy=100, pp=20, proba_effect=10)

    def effect(self):
        """
        High critical hit ratio. May poison opponent.
        """
        pass
