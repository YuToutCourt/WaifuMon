from ..move import Move
from waifu_types.type import Type

class RockPolish(Move):
    def __init__(self):
        super().__init__("Rock Polish", type=Type.ROCK, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Speed.
        """
        pass
