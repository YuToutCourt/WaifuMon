from ..move import Move
from waifu_types.type import Type

class HoneClaws(Move):
    def __init__(self):
        super().__init__("Hone Claws", type=Type.DARK, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and Accuracy.
        """
        pass
