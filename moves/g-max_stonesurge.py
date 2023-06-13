from .move import Move
from waifu_types.type import Type

class G-MaxStonesurge(Move):
    def __init__(self):
        super().__init__("G-Max Stonesurge", type=Type.WATER, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Drednaw-exclusive G-Max Move. Sets up Stealth Rock.
        """
        pass
