from .move import Move
from waifu_types.type import Type

class Fly(Move):
    def __init__(self):
        super().__init__("Fly", type=Type.FLYING, power=90, accuracy=95, pp=15, proba_effect=100)

    def effect(self):
        """
        Flies up on first turn, attacks on second turn.
        """
        pass
