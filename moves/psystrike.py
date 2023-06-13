from .move import Move
from waifu_types.type import Type

class Psystrike(Move):
    def __init__(self):
        super().__init__("Psystrike", type=Type.PSYCHIC, power=100, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Inflicts damage based on the target's Defense, not Special Defense.
        """
        pass
