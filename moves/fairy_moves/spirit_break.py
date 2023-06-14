from ..move import Move
from waifu_types.type import Type

class SpiritBreak(Move):
    def __init__(self):
        super().__init__("Spirit Break", type=Type.FAIRY, power=75, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
