from ..move import Move
from waifu_types.type import Type

class RockThrow(Move):
    def __init__(self):
        super().__init__("Rock Throw", type=Type.ROCK, power=50, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        
        """
        pass
