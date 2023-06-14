from ..move import Move
from waifu_types.type import Type

class Supersonic(Move):
    def __init__(self):
        super().__init__("Supersonic", type=Type.NORMAL, power=0, accuracy=55, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
