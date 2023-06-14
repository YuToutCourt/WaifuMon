from ..move import Move
from waifu_types.type import Type

class Geomancy(Move):
    def __init__(self):
        super().__init__("Geomancy", type=Type.FAIRY, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Charges on first turn, sharply raises user's Sp. Attack, Sp. Defense and Speed on the second.
        """
        pass
