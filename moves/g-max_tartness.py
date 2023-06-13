from .move import Move
from waifu_types.type import Type

class G-MaxTartness(Move):
    def __init__(self):
        super().__init__("G-Max Tartness", type=Type.GRASS, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Flapple-exclusive G-Max Move. Reduces opponents' evasiveness.
        """
        pass
