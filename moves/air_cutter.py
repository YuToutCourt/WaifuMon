from .move import Move
from waifu_types.type import Type

class AirCutter(Move):
    def __init__(self):
        super().__init__("Air Cutter", type=Type.FLYING, power=60, accuracy=95, pp=25, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
