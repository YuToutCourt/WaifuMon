from .move import Move
from waifu_types.type import Type

class SpitUp(Move):
    def __init__(self):
        super().__init__("Spit Up", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Power depends on how many times the user performed Stockpile.
        """
        pass
