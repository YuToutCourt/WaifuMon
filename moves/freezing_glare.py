from .move import Move
from waifu_types.type import Type

class FreezingGlare(Move):
    def __init__(self):
        super().__init__("Freezing Glare", type=Type.PSYCHIC, power=90, accuracy=100, pp=10, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
