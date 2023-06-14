from ..move import Move
from waifu_types.type import Type

class AquaTail(Move):
    def __init__(self):
        super().__init__("Aqua Tail", type=Type.WATER, power=90, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
