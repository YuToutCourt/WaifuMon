from ..move import Move
from waifu_types.type import Type

class FilletAway(Move):
    def __init__(self):
        super().__init__("Fillet Away", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers HP but sharply boosts Attack, Special Attack, and Speed.
        """
        pass
