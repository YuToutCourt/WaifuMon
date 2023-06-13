from .move import Move
from waifu_types.type import Type

class WaterShuriken(Move):
    def __init__(self):
        super().__init__("Water Shuriken", type=Type.WATER, power=15, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
