from ..move import Move
from waifu_types.type import Type

class G-MaxFoamBurst(Move):
    def __init__(self):
        super().__init__("G-Max Foam Burst", type=Type.WATER, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Kingler-exclusive G-Max Move. Harshly lowers opponents' Speed.
        """
        pass
