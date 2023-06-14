from ..move import Move
from waifu_types.type import Type

class Megahorn(Move):
    def __init__(self):
        super().__init__("Megahorn", type=Type.BUG, power=120, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
