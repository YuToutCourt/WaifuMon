from ..move import Move
from waifu_types.type import Type

class SubzeroSlammer(Move):
    def __init__(self):
        super().__init__("Subzero Slammer", type=Type.ICE, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Ice type Z-Move.
        """
        pass
