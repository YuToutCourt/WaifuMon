from .move import Move
from waifu_types.type import Type

class SolarBeam(Move):
    def __init__(self):
        super().__init__("Solar Beam", type=Type.GRASS, power=120, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Charges on first turn, attacks on second.
        """
        pass
