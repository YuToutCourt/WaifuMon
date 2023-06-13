from .move import Move
from waifu_types.type import Type

class Whirlpool(Move):
    def __init__(self):
        super().__init__("Whirlpool", type=Type.WATER, power=35, accuracy=85, pp=15, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
