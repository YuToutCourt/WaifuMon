from ..move import Move
from waifu_types.type import Type

class Thunderbolt(Move):
    def __init__(self):
        super().__init__("Thunderbolt", type=Type.ELECTRIC, power=90, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
