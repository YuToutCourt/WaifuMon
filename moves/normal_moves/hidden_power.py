from ..move import Move
from waifu_types.type import Type

class HiddenPower(Move):
    def __init__(self):
        super().__init__("Hidden Power", type=Type.NORMAL, power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Type and power depends on user's IVs.
        """
        pass
