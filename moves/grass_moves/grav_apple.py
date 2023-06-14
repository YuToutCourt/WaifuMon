from ..move import Move
from waifu_types.type import Type

class GravApple(Move):
    def __init__(self):
        super().__init__("Grav Apple", type=Type.GRASS, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers the opponent's Defense stat.
        """
        pass
