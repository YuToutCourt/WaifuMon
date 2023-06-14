from ..move import Move
from waifu_types.type import Type

class Nuzzle(Move):
    def __init__(self):
        super().__init__("Nuzzle", type=Type.ELECTRIC, power=20, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
