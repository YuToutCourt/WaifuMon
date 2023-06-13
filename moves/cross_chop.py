from .move import Move
from waifu_types.type import Type

class CrossChop(Move):
    def __init__(self):
        super().__init__("Cross Chop", type=Type.FIGHTING, power=100, accuracy=80, pp=5, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
