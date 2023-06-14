from ..move import Move
from waifu_types.type import Type

class PsychoBoost(Move):
    def __init__(self):
        super().__init__("Psycho Boost", type=Type.PSYCHIC, power=140, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers user's Special Attack.
        """
        pass
