from ..move import Move
from waifu_types.type import Type

class PollenPuff(Move):
    def __init__(self):
        super().__init__("Pollen Puff", type=Type.BUG, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage to opponent or restores HP of teammate.
        """
        pass
