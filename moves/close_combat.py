from .move import Move
from waifu_types.type import Type

class CloseCombat(Move):
    def __init__(self):
        super().__init__("Close Combat", type=Type.FIGHTING, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense and Special Defense.
        """
        pass
