from .move import Move
from waifu_types.type import Type

class RockTomb(Move):
    def __init__(self):
        super().__init__("Rock Tomb", type=Type.ROCK, power=60, accuracy=95, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
