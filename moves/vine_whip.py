from .move import Move
from waifu_types.type import Type

class VineWhip(Move):
    def __init__(self):
        super().__init__("Vine Whip", type=Type.GRASS, power=45, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
