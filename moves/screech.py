from .move import Move
from waifu_types.type import Type

class Screech(Move):
    def __init__(self):
        super().__init__("Screech", type=Type.NORMAL, power=0, accuracy=85, pp=40, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Defense.
        """
        pass
