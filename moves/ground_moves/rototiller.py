from ..move import Move
from waifu_types.type import Type

class Rototiller(Move):
    def __init__(self):
        super().__init__("Rototiller", type=Type.GROUND, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises Attack and Special Attack of Grass-types.
        """
        pass
