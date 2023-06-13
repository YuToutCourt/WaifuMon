from .move import Move
from waifu_types.type import Type

class Psyshock(Move):
    def __init__(self):
        super().__init__("Psyshock", type=Type.PSYCHIC, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Inflicts damage based on the target's Defense, not Special Defense.
        """
        pass
