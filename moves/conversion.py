from .move import Move
from waifu_types.type import Type

class Conversion(Move):
    def __init__(self):
        super().__init__("Conversion", type=Type.NORMAL, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Changes user's type to that of its first move.
        """
        pass
