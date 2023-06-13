from .move import Move
from waifu_types.type import Type

class ContinentalCrush(Move):
    def __init__(self):
        super().__init__("Continental Crush", type=Type.ROCK, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Rock type Z-Move.
        """
        pass
