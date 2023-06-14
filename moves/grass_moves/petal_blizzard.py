from ..move import Move
from waifu_types.type import Type

class PetalBlizzard(Move):
    def __init__(self):
        super().__init__("Petal Blizzard", type=Type.GRASS, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent Pok�mon.
        """
        pass
