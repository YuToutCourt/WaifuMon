from ..move import Move
from waifu_types.type import Type

class ShatteredPsyche(Move):
    def __init__(self):
        super().__init__("Shattered Psyche", type=Type.PSYCHIC, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Psychic type Z-Move.
        """
        pass
