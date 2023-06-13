from .move import Move
from waifu_types.type import Type

class Absorb(Move):
    def __init__(self):
        super().__init__("Absorb", type=Type.GRASS, power=20, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass