from ..move import Move
from waifu_types.type import Type

class DragonBreath(Move):
    def __init__(self):
        super().__init__("Dragon Breath", type=Type.DRAGON, power=60, accuracy=100, pp=20, priority=0, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
