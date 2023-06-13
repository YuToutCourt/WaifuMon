from .move import Move
from waifu_types.type import Type

class RazorWind(Move):
    def __init__(self):
        super().__init__("Razor Wind", type=Type.NORMAL, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Charges on first turn, attacks on second. High critical hit ratio.
        """
        pass
