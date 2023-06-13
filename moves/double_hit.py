from .move import Move
from waifu_types.type import Type

class DoubleHit(Move):
    def __init__(self):
        super().__init__("Double Hit", type=Type.NORMAL, power=35, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
