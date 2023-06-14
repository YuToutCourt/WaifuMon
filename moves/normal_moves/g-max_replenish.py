from ..move import Move
from waifu_types.type import Type

class G-MaxReplenish(Move):
    def __init__(self):
        super().__init__("G-Max Replenish", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Snorlax-exclusive G-Max Move. Recycles Berries.
        """
        pass
