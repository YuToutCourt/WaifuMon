from ..move import Move
from waifu_types.type import Type

class TailSlap(Move):
    def __init__(self):
        super().__init__("Tail Slap", type=Type.NORMAL, power=25, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
