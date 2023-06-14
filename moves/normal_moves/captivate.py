from ..move import Move
from waifu_types.type import Type

class Captivate(Move):
    def __init__(self):
        super().__init__("Captivate", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Special Attack if opposite gender.
        """
        pass
