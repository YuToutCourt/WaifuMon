from ..move import Move
from waifu_types.type import Type

class ThunderCage(Move):
    def __init__(self):
        super().__init__("Thunder Cage", type=Type.ELECTRIC, power=80, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage and traps opponent, damaging them for 4-5 turns.
        """
        pass
