from .move import Move
from waifu_types.type import Type

class Imprison(Move):
    def __init__(self):
        super().__init__("Imprison", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Opponent is unable to use moves that the user also knows.
        """
        pass
