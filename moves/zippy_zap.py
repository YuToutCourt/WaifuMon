from .move import Move
from waifu_types.type import Type

class ZippyZap(Move):
    def __init__(self):
        super().__init__("Zippy Zap", type=Type.ELECTRIC, power=50, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass
