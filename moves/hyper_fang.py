from .move import Move
from waifu_types.type import Type

class HyperFang(Move):
    def __init__(self):
        super().__init__("Hyper Fang", type=Type.NORMAL, power=80, accuracy=90, pp=15, proba_effect=10)

    def effect(self):
        """
        May cause flinching.
        """
        pass
