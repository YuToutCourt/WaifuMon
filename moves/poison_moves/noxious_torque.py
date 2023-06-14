from ..move import Move
from waifu_types.type import Type

class NoxiousTorque(Move):
    def __init__(self):
        super().__init__("Noxious Torque", type=Type.POISON, power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
