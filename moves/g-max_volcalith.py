from .move import Move
from waifu_types.type import Type

class G-MaxVolcalith(Move):
    def __init__(self):
        super().__init__("G-Max Volcalith", type=Type.ROCK, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Coalossal-exclusive G-Max Move. Deals damage for 4 turns.
        """
        pass
