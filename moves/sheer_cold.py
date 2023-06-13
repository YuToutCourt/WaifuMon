from .move import Move
from waifu_types.type import Type

class SheerCold(Move):
    def __init__(self):
        super().__init__("Sheer Cold", type=Type.ICE, power=0, accuracy=30, pp=5, proba_effect=100)

    def effect(self):
        """
        One-Hit-KO, if it hits.
        """
        pass
