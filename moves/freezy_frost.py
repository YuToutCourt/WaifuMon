from .move import Move
from waifu_types.type import Type

class FreezyFrost(Move):
    def __init__(self):
        super().__init__("Freezy Frost", type=Type.ICE, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Resets all stat changes.
        """
        pass
