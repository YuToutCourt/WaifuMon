from .move import Move
from waifu_types.type import Type

class HydroSteam(Move):
    def __init__(self):
        super().__init__("Hydro Steam", type=Type.WATER, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Power increases in harsh sunlight.
        """
        pass
