from .move import Move
from waifu_types.type import Type

class ThunderPunch(Move):
    def __init__(self):
        super().__init__("Thunder Punch", type=Type.ELECTRIC, power=75, accuracy=100, pp=15, proba_effect=10)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
