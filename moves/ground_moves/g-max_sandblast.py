from ..move import Move
from waifu_types.type import Type

class G-MaxSandblast(Move):
    def __init__(self):
        super().__init__("G-Max Sandblast", type=Type.GROUND, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Sandaconda-exclusive G-Max Move. Traps opponents for 4-5 turns.
        """
        pass
