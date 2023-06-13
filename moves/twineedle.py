from .move import Move
from waifu_types.type import Type

class Twineedle(Move):
    def __init__(self):
        super().__init__("Twineedle", type=Type.BUG, power=25, accuracy=100, pp=20, proba_effect=20)

    def effect(self):
        """
        Hits twice in one turn. May poison opponent.
        """
        pass
