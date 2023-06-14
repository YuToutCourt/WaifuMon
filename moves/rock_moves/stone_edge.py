from ..move import Move
from waifu_types.type import Type

class StoneEdge(Move):
    def __init__(self):
        super().__init__("Stone Edge", type=Type.ROCK, power=100, accuracy=80, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
