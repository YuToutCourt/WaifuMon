from ..move import Move
from waifu_types.type import Type

class TakeDown(Move):
    def __init__(self):
        super().__init__("Take Down", type=Type.NORMAL, power=90, accuracy=85, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
