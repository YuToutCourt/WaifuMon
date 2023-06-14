from ..move import Move
from waifu_types.type import Type

class GunkShot(Move):
    def __init__(self):
        super().__init__("Gunk Shot", type=Type.POISON, power=120, accuracy=80, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        May poison opponent.
        """
        pass
