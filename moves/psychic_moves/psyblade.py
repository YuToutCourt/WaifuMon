from ..move import Move
from waifu_types.type import Type

class Psyblade(Move):
    def __init__(self):
        super().__init__("Psyblade", type=Type.PSYCHIC, power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases on Electric Terrain.
        """
        pass
