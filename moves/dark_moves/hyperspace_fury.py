from ..move import Move
from waifu_types.type import Type

class HyperspaceFury(Move):
    def __init__(self):
        super().__init__("Hyperspace Fury", type=Type.DARK, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense. Can strike through Protect/Detect.
        """
        pass
