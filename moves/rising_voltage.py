from .move import Move
from waifu_types.type import Type

class RisingVoltage(Move):
    def __init__(self):
        super().__init__("Rising Voltage", type=Type.ELECTRIC, power=70, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Power doubles on Electric Terrain.
        """
        pass
