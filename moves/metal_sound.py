from .move import Move
from waifu_types.type import Type

class MetalSound(Move):
    def __init__(self):
        super().__init__("Metal Sound", type=Type.STEEL, power=0, accuracy=85, pp=40, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Special Defense.
        """
        pass
