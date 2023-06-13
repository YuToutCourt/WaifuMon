from .move import Move
from waifu_types.type import Type

class MagicalTorque(Move):
    def __init__(self):
        super().__init__("Magical Torque", type=Type.FAIRY, power=100, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
