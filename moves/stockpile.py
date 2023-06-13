from .move import Move
from waifu_types.type import Type

class Stockpile(Move):
    def __init__(self):
        super().__init__("Stockpile", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Stores energy for use with Spit Up and Swallow.
        """
        pass
