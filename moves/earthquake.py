from .move import Move
from waifu_types.type import Type

class Earthquake(Move):
    def __init__(self):
        super().__init__("Earthquake", type=Type.GROUND, power=100, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Power is doubled if opponent is underground from using Dig.
        """
        pass
