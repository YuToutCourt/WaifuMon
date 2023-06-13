from .move import Move
from waifu_types.type import Type

class SacredSword(Move):
    def __init__(self):
        super().__init__("Sacred Sword", type=Type.FIGHTING, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Ignores opponent's stat changes.
        """
        pass
