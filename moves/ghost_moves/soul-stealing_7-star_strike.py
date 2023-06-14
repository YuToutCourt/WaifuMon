from ..move import Move
from waifu_types.type import Type

class Soul-Stealing7-StarStrike(Move):
    def __init__(self):
        super().__init__("Soul-Stealing 7-Star Strike", type=Type.GHOST, power=195, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Marshadow-exclusive Z-Move.
        """
        pass
