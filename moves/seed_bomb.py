from .move import Move
from waifu_types.type import Type

class SeedBomb(Move):
    def __init__(self):
        super().__init__("Seed Bomb", type=Type.GRASS, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
