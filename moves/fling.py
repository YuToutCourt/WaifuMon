from .move import Move
from waifu_types.type import Type

class Fling(Move):
    def __init__(self):
        super().__init__("Fling", type=Type.DARK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Power depends on held item.
        """
        pass
