from ..move import Move
from waifu_types.type import Type

class G-MaxCentiferno(Move):
    def __init__(self):
        super().__init__("G-Max Centiferno", type=Type.FIRE, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Centiskorch-exclusive G-Max Move. Traps opponents for 4-5 turns.
        """
        pass
