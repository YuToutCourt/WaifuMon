from ..move import Move
from waifu_types.type import Type

class Endure(Move):
    def __init__(self):
        super().__init__("Endure", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Always left with at least 1 HP, but may fail if used consecutively.
        """
        pass
