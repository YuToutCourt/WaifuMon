from .move import Move
from waifu_types.type import Type

class NightSlash(Move):
    def __init__(self):
        super().__init__("Night Slash", type=Type.DARK, power=70, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
