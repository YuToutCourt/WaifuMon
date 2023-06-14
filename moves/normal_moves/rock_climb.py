from ..move import Move
from waifu_types.type import Type

class RockClimb(Move):
    def __init__(self):
        super().__init__("Rock Climb", type=Type.NORMAL, power=90, accuracy=85, pp=20, priority=0, proba_effect=20)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
