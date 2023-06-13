from .move import Move
from waifu_types.type import Type

class X-Scissor(Move):
    def __init__(self):
        super().__init__("X-Scissor", type=Type.BUG, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
