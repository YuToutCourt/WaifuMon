from .move import Move
from waifu_types.type import Type

class HammerArm(Move):
    def __init__(self):
        super().__init__("Hammer Arm", type=Type.FIGHTING, power=100, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Lowers user's Speed.
        """
        pass
