from .move import Move
from waifu_types.type import Type

class Moonblast(Move):
    def __init__(self):
        super().__init__("Moonblast", type=Type.FAIRY, power=95, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Special Attack.
        """
        pass
