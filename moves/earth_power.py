from .move import Move
from waifu_types.type import Type

class EarthPower(Move):
    def __init__(self):
        super().__init__("Earth Power", type=Type.GROUND, power=90, accuracy=100, pp=10, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Special Defense.
        """
        pass
