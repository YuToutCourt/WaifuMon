from ..move import Move
from waifu_types.type import Type

class MaxOvergrowth(Move):
    def __init__(self):
        super().__init__("Max Overgrowth", type=Type.GRASS, power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Grass type Dynamax move. Summons Grassy Terrain.
        """
        pass
