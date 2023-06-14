from ..move import Move
from waifu_types.type import Type

class PowerWhip(Move):
    def __init__(self):
        super().__init__("Power Whip", type=Type.GRASS, power=120, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
