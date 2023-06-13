from .move import Move
from waifu_types.type import Type

class Barrier(Move):
    def __init__(self):
        super().__init__("Barrier", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Defense.
        """
        pass
