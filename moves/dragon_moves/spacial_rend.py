from ..move import Move
from waifu_types.type import Type

class SpacialRend(Move):
    def __init__(self):
        super().__init__("Spacial Rend", type=Type.DRAGON, power=100, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
