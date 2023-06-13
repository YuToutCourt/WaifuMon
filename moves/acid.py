from .move import Move
from waifu_types.type import Type

class Acid(Move):
    def __init__(self):
        super().__init__("Acid", type=Type.POISON, power=40, accuracy=100, pp=30, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
