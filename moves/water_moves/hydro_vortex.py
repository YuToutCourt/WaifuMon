from ..move import Move
from waifu_types.type import Type

class HydroVortex(Move):
    def __init__(self):
        super().__init__("Hydro Vortex", type=Type.WATER, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Water type Z-Move.
        """
        pass
