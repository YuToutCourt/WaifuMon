from .move import Move
from waifu_types.type import Type

class TripleArrows(Move):
    def __init__(self):
        super().__init__("Triple Arrows", type=Type.FIGHTING, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Raises critical hit ratio and lowers target's Defense.
        """
        pass
