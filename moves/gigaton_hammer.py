from .move import Move
from waifu_types.type import Type

class GigatonHammer(Move):
    def __init__(self):
        super().__init__("Gigaton Hammer", type=Type.STEEL, power=160, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Cannot be used twice in a row.
        """
        pass
