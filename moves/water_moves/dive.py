from ..move import Move
from waifu_types.type import Type

class Dive(Move):
    def __init__(self):
        super().__init__("Dive", type=Type.WATER, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Dives underwater on first turn, attacks on second turn.
        """
        pass
