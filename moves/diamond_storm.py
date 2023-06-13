from .move import Move
from waifu_types.type import Type

class DiamondStorm(Move):
    def __init__(self):
        super().__init__("Diamond Storm", type=Type.ROCK, power=100, accuracy=95, pp=5, proba_effect=50)

    def effect(self):
        """
        May sharply raise user's Defense.
        """
        pass
