from .move import Move
from waifu_types.type import Type

class WaterPulse(Move):
    def __init__(self):
        super().__init__("Water Pulse", type=Type.WATER, power=60, accuracy=100, pp=20, proba_effect=20)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
