from .move import Move
from waifu_types.type import Type

class SpiritShackle(Move):
    def __init__(self):
        super().__init__("Spirit Shackle", type=Type.GHOST, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Prevents the opponent from switching out.
        """
        pass
