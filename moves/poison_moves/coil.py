from ..move import Move
from waifu_types.type import Type

class Coil(Move):
    def __init__(self):
        super().__init__("Coil", type=Type.POISON, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack, Defense and Accuracy.
        """
        pass
