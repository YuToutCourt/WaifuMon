from .move import Move
from waifu_types.type import Type

class ShadowForce(Move):
    def __init__(self):
        super().__init__("Shadow Force", type=Type.GHOST, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Disappears on first turn, attacks on second. Can strike through Protect/Detect.
        """
        pass
