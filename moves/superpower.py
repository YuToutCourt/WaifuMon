from .move import Move
from waifu_types.type import Type

class Superpower(Move):
    def __init__(self):
        super().__init__("Superpower", type=Type.FIGHTING, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Lowers user's Attack and Defense.
        """
        pass
