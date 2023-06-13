from .move import Move
from waifu_types.type import Type

class Substitute(Move):
    def __init__(self):
        super().__init__("Substitute", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Uses HP to creates a decoy that takes hits.
        """
        pass
