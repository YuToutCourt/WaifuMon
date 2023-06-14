from ..move import Move
from waifu_types.type import Type

class StruggleBug(Move):
    def __init__(self):
        super().__init__("Struggle Bug", type=Type.BUG, power=50, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
