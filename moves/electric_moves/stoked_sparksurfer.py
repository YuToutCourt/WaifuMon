from ..move import Move
from waifu_types.type import Type

class StokedSparksurfer(Move):
    def __init__(self):
        super().__init__("Stoked Sparksurfer", type=Type.ELECTRIC, power=175, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Alolan Raichu-exclusive Electric type Z-Move.
        """
        pass
