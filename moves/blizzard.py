from .move import Move
from waifu_types.type import Type

class Blizzard(Move):
    def __init__(self):
        super().__init__("Blizzard", type=Type.ICE, power=110, accuracy=70, pp=5, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
