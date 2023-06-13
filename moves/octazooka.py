from .move import Move
from waifu_types.type import Type

class Octazooka(Move):
    def __init__(self):
        super().__init__("Octazooka", type=Type.WATER, power=65, accuracy=85, pp=10, proba_effect=50)

    def effect(self):
        """
        May lower opponent's Accuracy.
        """
        pass
