from ..move import Move
from waifu_types.type import Type

class IcicleCrash(Move):
    def __init__(self):
        super().__init__("Icicle Crash", type=Type.ICE, power=85, accuracy=90, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass