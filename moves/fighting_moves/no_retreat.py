from ..move import Move
from waifu_types.type import Type

class NoRetreat(Move):
    def __init__(self):
        super().__init__("No Retreat", type=Type.FIGHTING, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises all stats but user cannot switch out.
        """
        pass
