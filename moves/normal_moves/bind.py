from ..move import Move
from waifu_types.type import Type

class Bind(Move):
    def __init__(self):
        super().__init__("Bind", type=Type.NORMAL, power=15, accuracy=85, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
