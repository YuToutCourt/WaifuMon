from .move import Move
from waifu_types.type import Type

class BrickBreak(Move):
    def __init__(self):
        super().__init__("Brick Break", type=Type.FIGHTING, power=75, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Breaks through Reflect and Light Screen barriers.
        """
        pass
