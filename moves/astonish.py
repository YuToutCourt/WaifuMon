from .move import Move
from waifu_types.type import Type

class Astonish(Move):
    def __init__(self):
        super().__init__("Astonish", type=Type.GHOST, power=30, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
