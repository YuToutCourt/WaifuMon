from ..move import Move
from waifu_types.type import Type

class Crunch(Move):
    def __init__(self):
        super().__init__("Crunch", type=Type.DARK, power=80, accuracy=100, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
