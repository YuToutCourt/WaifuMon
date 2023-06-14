from ..move import Move
from waifu_types.type import Type

class WaterSport(Move):
    def __init__(self):
        super().__init__("Water Sport", type=Type.WATER, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Weakens the power of Fire-type moves.
        """
        pass
