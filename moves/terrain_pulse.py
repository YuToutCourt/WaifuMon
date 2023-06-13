from .move import Move
from waifu_types.type import Type

class TerrainPulse(Move):
    def __init__(self):
        super().__init__("Terrain Pulse", type=Type.NORMAL, power=50, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Type and power change depending on the Terrain in effect.
        """
        pass
