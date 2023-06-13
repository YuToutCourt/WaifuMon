from .move import Move
from waifu_types.type import Type

class RazorLeaf(Move):
    def __init__(self):
        super().__init__("Razor Leaf", type=Type.GRASS, power=55, accuracy=95, pp=25, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
