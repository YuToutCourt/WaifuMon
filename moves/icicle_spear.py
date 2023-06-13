from .move import Move
from waifu_types.type import Type

class IcicleSpear(Move):
    def __init__(self):
        super().__init__("Icicle Spear", type=Type.ICE, power=25, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
