from .move import Move
from waifu_types.type import Type

class SearingShot(Move):
    def __init__(self):
        super().__init__("Searing Shot", type=Type.FIRE, power=100, accuracy=100, pp=5, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
