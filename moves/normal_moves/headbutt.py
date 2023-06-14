from ..move import Move
from waifu_types.type import Type

class Headbutt(Move):
    def __init__(self):
        super().__init__("Headbutt", type=Type.NORMAL, power=70, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
