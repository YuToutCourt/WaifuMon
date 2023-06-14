from ..move import Move
from waifu_types.type import Type

class SeismicToss(Move):
    def __init__(self):
        super().__init__("Seismic Toss", type=Type.FIGHTING, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Inflicts damage equal to user's level.
        """
        pass
