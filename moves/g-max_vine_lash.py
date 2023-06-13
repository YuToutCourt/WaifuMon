from .move import Move
from waifu_types.type import Type

class G-MaxVineLash(Move):
    def __init__(self):
        super().__init__("G-Max Vine Lash", type=Type.GRASS, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Venusaur-exclusive G-Max Move. Damages non-Grass types for 4 turns.
        """
        pass
