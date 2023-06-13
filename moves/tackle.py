from .move import Move
from waifu_types.type import Type

class Tackle(Move):
    def __init__(self):
        super().__init__("Tackle", type=Type.NORMAL, power=40, accuracy=100, pp=35, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
