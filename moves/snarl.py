from .move import Move
from waifu_types.type import Type

class Snarl(Move):
    def __init__(self):
        super().__init__("Snarl", type=Type.DARK, power=55, accuracy=95, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
