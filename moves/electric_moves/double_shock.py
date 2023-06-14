from ..move import Move
from waifu_types.type import Type

class DoubleShock(Move):
    def __init__(self):
        super().__init__("Double Shock", type=Type.ELECTRIC, power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        After using this move, the user will no longer be Electric type.
        """
        pass
