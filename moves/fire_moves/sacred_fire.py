from ..move import Move
from waifu_types.type import Type

class SacredFire(Move):
    def __init__(self):
        super().__init__("Sacred Fire", type=Type.FIRE, power=100, accuracy=95, pp=5, priority=0, proba_effect=50)

    def effect(self):
        """
        May burn opponent.
        """
        pass
