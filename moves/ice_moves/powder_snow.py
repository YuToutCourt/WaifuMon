from ..move import Move
from waifu_types.type import Type

class PowderSnow(Move):
    def __init__(self):
        super().__init__("Powder Snow", type=Type.ICE, power=40, accuracy=100, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
