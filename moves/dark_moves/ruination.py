from ..move import Move
from waifu_types.type import Type

class Ruination(Move):
    def __init__(self):
        super().__init__("Ruination", type=Type.DARK, power=1, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves the opponent's HP.
        """
        pass
