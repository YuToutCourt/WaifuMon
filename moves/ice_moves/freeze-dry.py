from ..move import Move
from waifu_types.type import Type

class Freeze-Dry(Move):
    def __init__(self):
        super().__init__("Freeze-Dry", type=Type.ICE, power=70, accuracy=100, pp=20, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent. Super-effective against Water types.
        """
        pass
