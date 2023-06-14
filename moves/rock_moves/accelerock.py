from ..move import Move
from waifu_types.type import Type

class Accelerock(Move):
    def __init__(self):
        super().__init__("Accelerock", type=Type.ROCK, power=40, accuracy=100, pp=20, priority=1, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass
