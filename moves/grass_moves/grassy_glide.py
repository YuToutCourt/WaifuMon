from ..move import Move
from waifu_types.type import Type

class GrassyGlide(Move):
    def __init__(self):
        super().__init__("Grassy Glide", type=Type.GRASS, power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        High priority during Grassy Terrain.
        """
        pass
