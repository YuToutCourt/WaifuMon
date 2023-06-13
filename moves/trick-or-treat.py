from .move import Move
from waifu_types.type import Type

class Trick-or-Treat(Move):
    def __init__(self):
        super().__init__("Trick-or-Treat", type=Type.GHOST, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Adds Ghost type to opponent.
        """
        pass
