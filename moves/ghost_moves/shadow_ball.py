from ..move import Move
from waifu_types.type import Type

class ShadowBall(Move):
    def __init__(self):
        super().__init__("Shadow Ball", type=Type.GHOST, power=80, accuracy=100, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
