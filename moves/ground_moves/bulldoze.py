from ..move import Move
from waifu_types.type import Type

class Bulldoze(Move):
    def __init__(self):
        super().__init__("Bulldoze", type=Type.GROUND, power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
