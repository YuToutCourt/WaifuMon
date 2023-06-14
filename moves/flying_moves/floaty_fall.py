from ..move import Move
from waifu_types.type import Type

class FloatyFall(Move):
    def __init__(self):
        super().__init__("Floaty Fall", type=Type.FLYING, power=90, accuracy=95, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
