from ..move import Move
from waifu_types.type import Type

class Magnitude(Move):
    def __init__(self):
        super().__init__("Magnitude", type=Type.GROUND, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits with random power.
        """
        pass
