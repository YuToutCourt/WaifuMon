from ..move import Move
from waifu_types.type import Type

class Waterfall(Move):
    def __init__(self):
        super().__init__("Waterfall", type=Type.WATER, power=80, accuracy=100, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass
