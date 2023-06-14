from ..move import Move
from waifu_types.type import Type

class LightofRuin(Move):
    def __init__(self):
        super().__init__("Light of Ruin", type=Type.FAIRY, power=140, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
