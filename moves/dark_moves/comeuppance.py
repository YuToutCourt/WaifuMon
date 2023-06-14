from ..move import Move
from waifu_types.type import Type

class Comeuppance(Move):
    def __init__(self):
        super().__init__("Comeuppance", type=Type.DARK, power=1, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals more damage to the opponent that last inflicted damage on it.
        """
        pass
