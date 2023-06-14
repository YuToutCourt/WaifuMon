from ..move import Move
from waifu_types.type import Type

class MindBlown(Move):
    def __init__(self):
        super().__init__("Mind Blown", type=Type.FIRE, power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
