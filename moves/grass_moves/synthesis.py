from ..move import Move
from waifu_types.type import Type

class Synthesis(Move):
    def __init__(self):
        super().__init__("Synthesis", type=Type.GRASS, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers HP. Amount varies with the weather.
        """
        pass
