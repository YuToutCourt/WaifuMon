from .move import Move
from waifu_types.type import Type

class SnipeShot(Move):
    def __init__(self):
        super().__init__("Snipe Shot", type=Type.WATER, power=80, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Ignores moves and abilities that draw in moves. High critical hit ratio.
        """
        pass
