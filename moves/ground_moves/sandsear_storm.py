from ..move import Move
from waifu_types.type import Type

class SandsearStorm(Move):
    def __init__(self):
        super().__init__("Sandsear Storm", type=Type.GROUND, power=100, accuracy=80, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        May burn target.
        """
        pass
