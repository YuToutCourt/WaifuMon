from ..move import Move
from waifu_types.type import Type

class Foresight(Move):
    def __init__(self):
        super().__init__("Foresight", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Resets opponent's Evasiveness, and allows Normal- and Fighting-type attacks to hit Ghosts.
        """
        pass
