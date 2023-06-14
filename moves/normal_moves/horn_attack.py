from ..move import Move
from waifu_types.type import Type

class HornAttack(Move):
    def __init__(self):
        super().__init__("Horn Attack", type=Type.NORMAL, power=65, accuracy=100, pp=25, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
