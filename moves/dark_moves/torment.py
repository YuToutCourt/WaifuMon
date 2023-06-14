from ..move import Move
from waifu_types.type import Type

class Torment(Move):
    def __init__(self):
        super().__init__("Torment", type=Type.DARK, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot use the same move in a row.
        """
        pass
