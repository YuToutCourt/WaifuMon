from .move import Move
from waifu_types.type import Type

class ShadowBone(Move):
    def __init__(self):
        super().__init__("Shadow Bone", type=Type.GHOST, power=85, accuracy=100, pp=10, proba_effect=20)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
