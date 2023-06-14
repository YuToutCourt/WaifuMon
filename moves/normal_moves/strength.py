from ..move import Move
from waifu_types.type import Type

class Strength(Move):
    def __init__(self):
        super().__init__("Strength", type=Type.NORMAL, power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
