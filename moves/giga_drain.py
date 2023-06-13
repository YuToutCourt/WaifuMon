from .move import Move
from waifu_types.type import Type

class GigaDrain(Move):
    def __init__(self):
        super().__init__("Giga Drain", type=Type.GRASS, power=75, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on opponent.
        """
        pass
