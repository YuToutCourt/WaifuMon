from ..move import Move
from waifu_types.type import Type

class Electroweb(Move):
    def __init__(self):
        super().__init__("Electroweb", type=Type.ELECTRIC, power=55, accuracy=95, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
