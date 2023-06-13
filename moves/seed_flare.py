from .move import Move
from waifu_types.type import Type

class SeedFlare(Move):
    def __init__(self):
        super().__init__("Seed Flare", type=Type.GRASS, power=120, accuracy=85, pp=5, proba_effect=40)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
