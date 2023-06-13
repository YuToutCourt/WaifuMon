from .move import Move
from waifu_types.type import Type

class Forest'sCurse(Move):
    def __init__(self):
        super().__init__("Forest's Curse", type=Type.GRASS, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Adds Grass type to opponent.
        """
        pass
