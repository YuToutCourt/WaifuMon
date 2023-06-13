from .move import Move
from waifu_types.type import Type

class NaturePower(Move):
    def __init__(self):
        super().__init__("Nature Power", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Uses a certain move based on the current terrain.
        """
        pass
