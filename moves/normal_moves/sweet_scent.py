from ..move import Move
from waifu_types.type import Type

class SweetScent(Move):
    def __init__(self):
        super().__init__("Sweet Scent", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Evasiveness.
        """
        pass
