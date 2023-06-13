from .move import Move
from waifu_types.type import Type

class ConfuseRay(Move):
    def __init__(self):
        super().__init__("Confuse Ray", type=Type.GHOST, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
