from ..move import Move
from waifu_types.type import Type

class NightShade(Move):
    def __init__(self):
        super().__init__("Night Shade", type=Type.GHOST, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts damage equal to user's level.
        """
        pass
