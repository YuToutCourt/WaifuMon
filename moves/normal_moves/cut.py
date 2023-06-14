from ..move import Move
from waifu_types.type import Type

class Cut(Move):
    def __init__(self):
        super().__init__("Cut", type=Type.NORMAL, power=50, accuracy=95, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
