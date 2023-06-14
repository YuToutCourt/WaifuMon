from ..move import Move
from waifu_types.type import Type

class KowtowCleave(Move):
    def __init__(self):
        super().__init__("Kowtow Cleave", type=Type.DARK, power=85, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Always hits.
        """
        pass
