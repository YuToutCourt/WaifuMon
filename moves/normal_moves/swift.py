from ..move import Move
from waifu_types.type import Type

class Swift(Move):
    def __init__(self):
        super().__init__("Swift", type=Type.NORMAL, power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores Accuracy and Evasiveness.
        """
        pass
