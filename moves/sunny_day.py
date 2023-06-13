from .move import Move
from waifu_types.type import Type

class SunnyDay(Move):
    def __init__(self):
        super().__init__("Sunny Day", type=Type.FIRE, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Makes it sunny for 5 turns.
        """
        pass
