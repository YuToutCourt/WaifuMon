from ..move import Move
from waifu_types.type import Type

class BellyDrum(Move):
    def __init__(self):
        super().__init__("Belly Drum", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User loses 50% of its max HP, but Attack raises to maximum.
        """
        pass
