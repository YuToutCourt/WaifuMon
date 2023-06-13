from .move import Move
from waifu_types.type import Type

class SupersonicSkystrike(Move):
    def __init__(self):
        super().__init__("Supersonic Skystrike", type=Type.FLYING, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Flying type Z-Move.
        """
        pass
