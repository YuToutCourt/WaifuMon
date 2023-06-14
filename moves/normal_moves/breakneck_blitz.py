from ..move import Move
from waifu_types.type import Type

class BreakneckBlitz(Move):
    def __init__(self):
        super().__init__("Breakneck Blitz", type=Type.NORMAL, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Normal type Z-Move.
        """
        pass
