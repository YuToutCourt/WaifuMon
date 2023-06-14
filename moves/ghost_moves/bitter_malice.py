from ..move import Move
from waifu_types.type import Type

class BitterMalice(Move):
    def __init__(self):
        super().__init__("Bitter Malice", type=Type.GHOST, power=75, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts double damage if the target has a status condition.
        """
        pass
