from ..move import Move
from waifu_types.type import Type

class HeadSmash(Move):
    def __init__(self):
        super().__init__("Head Smash", type=Type.ROCK, power=150, accuracy=80, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
