from .move import Move
from waifu_types.type import Type

class Autotomize(Move):
    def __init__(self):
        super().__init__("Autotomize", type=Type.STEEL, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Reduces weight and sharply raises Speed.
        """
        pass
