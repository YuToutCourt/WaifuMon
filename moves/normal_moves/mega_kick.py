from ..move import Move
from waifu_types.type import Type

class MegaKick(Move):
    def __init__(self):
        super().__init__("Mega Kick", type=Type.NORMAL, power=120, accuracy=75, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
