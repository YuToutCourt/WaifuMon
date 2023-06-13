from .move import Move
from waifu_types.type import Type

class MagmaStorm(Move):
    def __init__(self):
        super().__init__("Magma Storm", type=Type.FIRE, power=100, accuracy=75, pp=5, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
