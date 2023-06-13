from .move import Move
from waifu_types.type import Type

class G-MaxSweetness(Move):
    def __init__(self):
        super().__init__("G-Max Sweetness", type=Type.GRASS, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Appletun-exclusive G-Max Move. Heals status conditions of user's team.
        """
        pass
