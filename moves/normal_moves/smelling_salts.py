from ..move import Move
from waifu_types.type import Type

class SmellingSalts(Move):
    def __init__(self):
        super().__init__("Smelling Salts", type=Type.NORMAL, power=70, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if opponent is paralyzed, but cures it.
        """
        pass