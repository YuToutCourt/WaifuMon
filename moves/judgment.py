from .move import Move
from waifu_types.type import Type

class Judgment(Move):
    def __init__(self):
        super().__init__("Judgment", type=Type.NORMAL, power=100, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Type depends on the Arceus Plate being held.
        """
        pass
