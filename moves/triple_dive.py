from .move import Move
from waifu_types.type import Type

class TripleDive(Move):
    def __init__(self):
        super().__init__("Triple Dive", type=Type.WATER, power=30, accuracy=95, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits 3 times in a row.
        """
        pass
