from .move import Move
from waifu_types.type import Type

class AuroraBeam(Move):
    def __init__(self):
        super().__init__("Aurora Beam", type=Type.ICE, power=65, accuracy=100, pp=20, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Attack.
        """
        pass
