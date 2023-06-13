from .move import Move
from waifu_types.type import Type

class StringShot(Move):
    def __init__(self):
        super().__init__("String Shot", type=Type.BUG, power=0, accuracy=95, pp=40, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Speed.
        """
        pass
