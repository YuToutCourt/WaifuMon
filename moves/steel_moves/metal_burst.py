from ..move import Move
from waifu_types.type import Type

class MetalBurst(Move):
    def __init__(self):
        super().__init__("Metal Burst", type=Type.STEEL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage equal to 1.5x opponent's attack.
        """
        pass
