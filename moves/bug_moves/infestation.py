from ..move import Move
from waifu_types.type import Type

class Infestation(Move):
    def __init__(self):
        super().__init__("Infestation", type=Type.BUG, power=20, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
