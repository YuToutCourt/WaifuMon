from .move import Move
from waifu_types.type import Type

class Spore(Move):
    def __init__(self):
        super().__init__("Spore", type=Type.GRASS, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
