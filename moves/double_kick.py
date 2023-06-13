from .move import Move
from waifu_types.type import Type

class DoubleKick(Move):
    def __init__(self):
        super().__init__("Double Kick", type=Type.FIGHTING, power=30, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
