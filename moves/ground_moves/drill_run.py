from ..move import Move
from waifu_types.type import Type

class DrillRun(Move):
    def __init__(self):
        super().__init__("Drill Run", type=Type.GROUND, power=80, accuracy=95, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
