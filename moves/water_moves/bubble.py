from ..move import Move
from waifu_types.type import Type

class Bubble(Move):
    def __init__(self):
        super().__init__("Bubble", type=Type.WATER, power=40, accuracy=100, pp=30, priority=0, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Speed.
        """
        pass
