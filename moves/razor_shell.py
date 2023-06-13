from .move import Move
from waifu_types.type import Type

class RazorShell(Move):
    def __init__(self):
        super().__init__("Razor Shell", type=Type.WATER, power=75, accuracy=95, pp=10, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
