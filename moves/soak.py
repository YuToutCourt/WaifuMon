from .move import Move
from waifu_types.type import Type

class Soak(Move):
    def __init__(self):
        super().__init__("Soak", type=Type.WATER, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Changes the target's type to water.
        """
        pass
