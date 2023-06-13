from .move import Move
from waifu_types.type import Type

class SmartStrike(Move):
    def __init__(self):
        super().__init__("Smart Strike", type=Type.STEEL, power=70, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        The user stabs the target with a sharp horn. This attack never misses.
        """
        pass
