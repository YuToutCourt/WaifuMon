from .move import Move
from waifu_types.type import Type

class NeedleArm(Move):
    def __init__(self):
        super().__init__("Needle Arm", type=Type.GRASS, power=60, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
