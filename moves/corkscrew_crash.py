from .move import Move
from waifu_types.type import Type

class CorkscrewCrash(Move):
    def __init__(self):
        super().__init__("Corkscrew Crash", type=Type.STEEL, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Steel type Z-Move.
        """
        pass
