from .move import Move
from waifu_types.type import Type

class Sludge(Move):
    def __init__(self):
        super().__init__("Sludge", type=Type.POISON, power=65, accuracy=100, pp=20, proba_effect=30)

    def effect(self):
        """
        May poison opponent.
        """
        pass
