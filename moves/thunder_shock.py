from .move import Move
from waifu_types.type import Type

class ThunderShock(Move):
    def __init__(self):
        super().__init__("Thunder Shock", type=Type.ELECTRIC, power=40, accuracy=100, pp=30, proba_effect=10)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
