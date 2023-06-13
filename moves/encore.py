from .move import Move
from waifu_types.type import Type

class Encore(Move):
    def __init__(self):
        super().__init__("Encore", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Forces opponent to keep using its last move for 3 turns.
        """
        pass
