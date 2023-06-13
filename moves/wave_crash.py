from .move import Move
from waifu_types.type import Type

class WaveCrash(Move):
    def __init__(self):
        super().__init__("Wave Crash", type=Type.WATER, power=120, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
