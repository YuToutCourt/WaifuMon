from ..move import Move
from waifu_types.type import Type

class RockSmash(Move):
    def __init__(self):
        super().__init__("Rock Smash", type=Type.FIGHTING, power=40, accuracy=100, pp=15, priority=0, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
