from .move import Move
from waifu_types.type import Type

class FreezeShock(Move):
    def __init__(self):
        super().__init__("Freeze Shock", type=Type.ICE, power=140, accuracy=90, pp=5, proba_effect=30)

    def effect(self):
        """
        Charges on first turn, attacks on second. May paralyze opponent.
        """
        pass
