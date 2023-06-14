from ..move import Move
from waifu_types.type import Type

class Chloroblast(Move):
    def __init__(self):
        super().__init__("Chloroblast", type=Type.GRASS, power=150, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
