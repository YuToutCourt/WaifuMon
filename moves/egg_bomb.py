from .move import Move
from waifu_types.type import Type

class EggBomb(Move):
    def __init__(self):
        super().__init__("Egg Bomb", type=Type.NORMAL, power=100, accuracy=75, pp=10, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
