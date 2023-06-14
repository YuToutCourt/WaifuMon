from ..move import Move
from waifu_types.type import Type

class Scratch(Move):
    def __init__(self):
        super().__init__("Scratch", type=Type.NORMAL, power=40, accuracy=100, pp=35, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
