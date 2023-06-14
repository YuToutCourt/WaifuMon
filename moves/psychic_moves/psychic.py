from ..move import Move
from waifu_types.type import Type

class Psychic(Move):
    def __init__(self):
        super().__init__("Psychic", type=Type.PSYCHIC, power=90, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
