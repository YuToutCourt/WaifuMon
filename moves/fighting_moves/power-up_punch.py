from ..move import Move
from waifu_types.type import Type

class Power-UpPunch(Move):
    def __init__(self):
        super().__init__("Power-Up Punch", type=Type.FIGHTING, power=40, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Attack.
        """
        pass
