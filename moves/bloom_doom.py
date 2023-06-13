from .move import Move
from waifu_types.type import Type

class BloomDoom(Move):
    def __init__(self):
        super().__init__("Bloom Doom", type=Type.GRASS, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Grass type Z-Move.
        """
        pass
