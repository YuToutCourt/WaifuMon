from ..move import Move
from waifu_types.type import Type

class DragonPulse(Move):
    def __init__(self):
        super().__init__("Dragon Pulse", type=Type.DRAGON, power=85, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
