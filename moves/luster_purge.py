from .move import Move
from waifu_types.type import Type

class LusterPurge(Move):
    def __init__(self):
        super().__init__("Luster Purge", type=Type.PSYCHIC, power=70, accuracy=100, pp=5, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
