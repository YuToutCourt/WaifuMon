from .move import Move
from waifu_types.type import Type

class Aeroblast(Move):
    def __init__(self):
        super().__init__("Aeroblast", type=Type.FLYING, power=100, accuracy=95, pp=5, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
