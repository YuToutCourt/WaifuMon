from ..move import Move
from waifu_types.type import Type

class MeanLook(Move):
    def __init__(self):
        super().__init__("Mean Look", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot flee or switch.
        """
        pass
