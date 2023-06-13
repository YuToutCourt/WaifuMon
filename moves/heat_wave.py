from .move import Move
from waifu_types.type import Type

class HeatWave(Move):
    def __init__(self):
        super().__init__("Heat Wave", type=Type.FIRE, power=95, accuracy=90, pp=10, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
