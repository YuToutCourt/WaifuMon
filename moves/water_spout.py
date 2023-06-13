from .move import Move
from waifu_types.type import Type

class WaterSpout(Move):
    def __init__(self):
        super().__init__("Water Spout", type=Type.WATER, power=150, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        The higher the user's HP, the higher the damage caused.
        """
        pass
