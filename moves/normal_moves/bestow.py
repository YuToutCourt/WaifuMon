from ..move import Move
from waifu_types.type import Type

class Bestow(Move):
    def __init__(self):
        super().__init__("Bestow", type=Type.NORMAL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Gives the user's held item to the target.
        """
        pass
