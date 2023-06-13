from .move import Move
from waifu_types.type import Type

class AquaRing(Move):
    def __init__(self):
        super().__init__("Aqua Ring", type=Type.WATER, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Restores a little HP each turn.
        """
        pass
