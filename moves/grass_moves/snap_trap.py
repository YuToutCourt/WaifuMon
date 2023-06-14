from ..move import Move
from waifu_types.type import Type

class SnapTrap(Move):
    def __init__(self):
        super().__init__("Snap Trap", type=Type.GRASS, power=35, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
