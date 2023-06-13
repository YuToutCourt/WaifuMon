from .move import Move
from waifu_types.type import Type

class ArmThrust(Move):
    def __init__(self):
        super().__init__("Arm Thrust", type=Type.FIGHTING, power=15, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
