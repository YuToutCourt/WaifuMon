from ..move import Move
from waifu_types.type import Type

class MachPunch(Move):
    def __init__(self):
        super().__init__("Mach Punch", type=Type.FIGHTING, power=40, accuracy=100, pp=30, priority=1, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass
