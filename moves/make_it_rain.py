from .move import Move
from waifu_types.type import Type

class MakeItRain(Move):
    def __init__(self):
        super().__init__("Make It Rain", type=Type.STEEL, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Lowers user's Special Attack. Money is earned after the battle.
        """
        pass
