from .move import Move
from waifu_types.type import Type

class RockSlide(Move):
    def __init__(self):
        super().__init__("Rock Slide", type=Type.ROCK, power=75, accuracy=90, pp=10, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
