from .move import Move
from waifu_types.type import Type

class MaxHailstorm(Move):
    def __init__(self):
        super().__init__("Max Hailstorm", type=Type.ICE, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Ice type Dynamax move. Summons hail.
        """
        pass
