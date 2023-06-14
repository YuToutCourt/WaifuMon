from ..move import Move
from waifu_types.type import Type

class OceanicOperetta(Move):
    def __init__(self):
        super().__init__("Oceanic Operetta", type=Type.WATER, power=195, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Primarina-exclusive Z-Move.
        """
        pass