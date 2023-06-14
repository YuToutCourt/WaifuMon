from ..move import Move
from waifu_types.type import Type

class MegaPunch(Move):
    def __init__(self):
        super().__init__("Mega Punch", type=Type.NORMAL, power=80, accuracy=85, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
