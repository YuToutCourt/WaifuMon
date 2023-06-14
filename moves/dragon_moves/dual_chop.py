from ..move import Move
from waifu_types.type import Type

class DualChop(Move):
    def __init__(self):
        super().__init__("Dual Chop", type=Type.DRAGON, power=40, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
