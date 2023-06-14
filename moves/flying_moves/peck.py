from ..move import Move
from waifu_types.type import Type

class Peck(Move):
    def __init__(self):
        super().__init__("Peck", type=Type.FLYING, power=35, accuracy=100, pp=35, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
