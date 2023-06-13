from .move import Move
from waifu_types.type import Type

class SandAttack(Move):
    def __init__(self):
        super().__init__("Sand Attack", type=Type.GROUND, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass
