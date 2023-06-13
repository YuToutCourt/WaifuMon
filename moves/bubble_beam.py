from .move import Move
from waifu_types.type import Type

class BubbleBeam(Move):
    def __init__(self):
        super().__init__("Bubble Beam", type=Type.WATER, power=65, accuracy=100, pp=20, proba_effect=10)

    def effect(self):
        """
        May lower opponent's Speed.
        """
        pass
