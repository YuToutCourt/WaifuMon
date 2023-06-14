from ..move import Move
from waifu_types.type import Type

class WoodHammer(Move):
    def __init__(self):
        super().__init__("Wood Hammer", type=Type.GRASS, power=120, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
