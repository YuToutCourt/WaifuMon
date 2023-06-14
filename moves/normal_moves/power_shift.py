from ..move import Move
from waifu_types.type import Type

class PowerShift(Move):
    def __init__(self):
        super().__init__("Power Shift", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Switches offensive and defensive stats.
        """
        pass
