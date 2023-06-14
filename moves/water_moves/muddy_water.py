from ..move import Move
from waifu_types.type import Type

class MuddyWater(Move):
    def __init__(self):
        super().__init__("Muddy Water", type=Type.WATER, power=90, accuracy=85, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
