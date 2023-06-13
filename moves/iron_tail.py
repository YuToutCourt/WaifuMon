from .move import Move
from waifu_types.type import Type

class IronTail(Move):
    def __init__(self):
        super().__init__("Iron Tail", type=Type.STEEL, power=100, accuracy=75, pp=15, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
