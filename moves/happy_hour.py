from .move import Move
from waifu_types.type import Type

class HappyHour(Move):
    def __init__(self):
        super().__init__("Happy Hour", type=Type.NORMAL, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Doubles prize money from trainer battles.
        """
        pass
