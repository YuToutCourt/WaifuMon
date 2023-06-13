from .move import Move
from waifu_types.type import Type

class EnergyBall(Move):
    def __init__(self):
        super().__init__("Energy Ball", type=Type.GRASS, power=90, accuracy=100, pp=10, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
