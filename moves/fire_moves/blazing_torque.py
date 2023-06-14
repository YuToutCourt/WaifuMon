from ..move import Move
from waifu_types.type import Type

class BlazingTorque(Move):
    def __init__(self):
        super().__init__("Blazing Torque", type=Type.FIRE, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
