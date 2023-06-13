from .move import Move
from waifu_types.type import Type

class GuardSplit(Move):
    def __init__(self):
        super().__init__("Guard Split", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Averages Defense and Special Defense with the target.
        """
        pass
