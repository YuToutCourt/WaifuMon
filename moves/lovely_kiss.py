from .move import Move
from waifu_types.type import Type

class LovelyKiss(Move):
    def __init__(self):
        super().__init__("Lovely Kiss", type=Type.NORMAL, power=0, accuracy=75, pp=10, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
