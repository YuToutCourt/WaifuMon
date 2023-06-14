from ..move import Move
from waifu_types.type import Type

class WaterGun(Move):
    def __init__(self):
        super().__init__("Water Gun", type=Type.WATER, power=40, accuracy=100, pp=25, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
