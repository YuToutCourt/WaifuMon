from ..move import Move
from waifu_types.type import Type

class Bite(Move):
    def __init__(self):
        super().__init__("Bite", type=Type.DARK, power=60, accuracy=100, pp=25, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
