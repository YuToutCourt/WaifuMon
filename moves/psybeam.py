from .move import Move
from waifu_types.type import Type

class Psybeam(Move):
    def __init__(self):
        super().__init__("Psybeam", type=Type.PSYCHIC, power=65, accuracy=100, pp=20, proba_effect=10)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
