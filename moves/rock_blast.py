from .move import Move
from waifu_types.type import Type

class RockBlast(Move):
    def __init__(self):
        super().__init__("Rock Blast", type=Type.ROCK, power=25, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
