from ..move import Move
from waifu_types.type import Type

class HeadCharge(Move):
    def __init__(self):
        super().__init__("Head Charge", type=Type.NORMAL, power=120, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
