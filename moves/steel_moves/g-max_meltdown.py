from ..move import Move
from waifu_types.type import Type

class G-MaxMeltdown(Move):
    def __init__(self):
        super().__init__("G-Max Meltdown", type=Type.STEEL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Melmetal-exclusive G-Max Move. Prevents opponents using the same move twice in a row.
        """
        pass
