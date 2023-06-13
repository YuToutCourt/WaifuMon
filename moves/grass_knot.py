from .move import Move
from waifu_types.type import Type

class GrassKnot(Move):
    def __init__(self):
        super().__init__("Grass Knot", type=Type.GRASS, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        The heavier the opponent, the stronger the attack.
        """
        pass
