from .move import Move
from waifu_types.type import Type

class MiracleEye(Move):
    def __init__(self):
        super().__init__("Miracle Eye", type=Type.PSYCHIC, power=0, accuracy=100, pp=40, proba_effect=100)

    def effect(self):
        """
        Resets opponent's Evasiveness, removes Dark's Psychic immunity.
        """
        pass
