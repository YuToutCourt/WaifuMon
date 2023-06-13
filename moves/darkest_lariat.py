from .move import Move
from waifu_types.type import Type

class DarkestLariat(Move):
    def __init__(self):
        super().__init__("Darkest Lariat", type=Type.DARK, power=85, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Ignores opponent's stat changes.
        """
        pass
