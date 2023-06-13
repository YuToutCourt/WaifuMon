from .move import Move
from waifu_types.type import Type

class Endeavor(Move):
    def __init__(self):
        super().__init__("Endeavor", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Reduces opponent's HP to same as user's.
        """
        pass
