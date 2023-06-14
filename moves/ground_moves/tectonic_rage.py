from ..move import Move
from waifu_types.type import Type

class TectonicRage(Move):
    def __init__(self):
        super().__init__("Tectonic Rage", type=Type.GROUND, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Ground type Z-Move.
        """
        pass
