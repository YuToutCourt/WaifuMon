from .move import Move
from waifu_types.type import Type

class Octolock(Move):
    def __init__(self):
        super().__init__("Octolock", type=Type.FIGHTING, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Defense and Special Defense every turn, and they cannot flee or switch out.
        """
        pass
