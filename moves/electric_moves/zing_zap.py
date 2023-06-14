from ..move import Move
from waifu_types.type import Type

class ZingZap(Move):
    def __init__(self):
        super().__init__("Zing Zap", type=Type.ELECTRIC, power=80, accuracy=100, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
