from ..move import Move
from waifu_types.type import Type

class TripleKick(Move):
    def __init__(self):
        super().__init__("Triple Kick", type=Type.FIGHTING, power=10, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits thrice in one turn at increasing power.
        """
        pass
