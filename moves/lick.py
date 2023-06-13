from .move import Move
from waifu_types.type import Type

class Lick(Move):
    def __init__(self):
        super().__init__("Lick", type=Type.GHOST, power=30, accuracy=100, pp=30, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
