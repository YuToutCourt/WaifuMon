from ..move import Move
from waifu_types.type import Type

class SpikeCannon(Move):
    def __init__(self):
        super().__init__("Spike Cannon", type=Type.NORMAL, power=20, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
