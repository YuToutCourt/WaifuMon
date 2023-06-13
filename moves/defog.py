from .move import Move
from waifu_types.type import Type

class Defog(Move):
    def __init__(self):
        super().__init__("Defog", type=Type.FLYING, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Evasiveness and clears fog.
        """
        pass
