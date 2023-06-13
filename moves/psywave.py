from .move import Move
from waifu_types.type import Type

class Psywave(Move):
    def __init__(self):
        super().__init__("Psywave", type=Type.PSYCHIC, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Inflicts damage 50-150% of user's level.
        """
        pass
