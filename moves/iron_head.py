from .move import Move
from waifu_types.type import Type

class IronHead(Move):
    def __init__(self):
        super().__init__("Iron Head", type=Type.STEEL, power=80, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
