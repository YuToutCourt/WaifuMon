from ..move import Move
from waifu_types.type import Type

class AuroraVeil(Move):
    def __init__(self):
        super().__init__("Aurora Veil", type=Type.ICE, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves damage from Physical and Special attacks for five turns.
        """
        pass