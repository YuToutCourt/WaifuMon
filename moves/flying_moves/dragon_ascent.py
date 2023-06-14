from ..move import Move
from waifu_types.type import Type

class DragonAscent(Move):
    def __init__(self):
        super().__init__("Dragon Ascent", type=Type.FLYING, power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense and Special Defense.
        """
        pass
