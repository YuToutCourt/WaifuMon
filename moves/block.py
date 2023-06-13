from .move import Move
from waifu_types.type import Type

class Block(Move):
    def __init__(self):
        super().__init__("Block", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Opponent cannot flee or switch.
        """
        pass
