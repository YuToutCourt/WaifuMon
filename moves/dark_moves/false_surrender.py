from ..move import Move
from waifu_types.type import Type

class FalseSurrender(Move):
    def __init__(self):
        super().__init__("False Surrender", type=Type.DARK, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass
