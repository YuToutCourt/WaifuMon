from ..move import Move
from waifu_types.type import Type

class VoltTackle(Move):
    def __init__(self):
        super().__init__("Volt Tackle", type=Type.ELECTRIC, power=120, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        User receives recoil damage. May paralyze opponent.
        """
        pass
