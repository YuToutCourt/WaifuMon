from ..move import Move
from waifu_types.type import Type

class FireBlast(Move):
    def __init__(self):
        super().__init__("Fire Blast", type=Type.FIRE, power=110, accuracy=85, pp=5, priority=0, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
