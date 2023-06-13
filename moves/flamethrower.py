from .move import Move
from waifu_types.type import Type

class Flamethrower(Move):
    def __init__(self):
        super().__init__("Flamethrower", type=Type.FIRE, power=90, accuracy=100, pp=15, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
