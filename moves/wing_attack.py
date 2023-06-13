from .move import Move
from waifu_types.type import Type

class WingAttack(Move):
    def __init__(self):
        super().__init__("Wing Attack", type=Type.FLYING, power=60, accuracy=100, pp=35, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
