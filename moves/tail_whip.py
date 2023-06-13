from .move import Move
from waifu_types.type import Type

class TailWhip(Move):
    def __init__(self):
        super().__init__("Tail Whip", type=Type.NORMAL, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Defense.
        """
        pass
