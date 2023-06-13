from .move import Move
from waifu_types.type import Type

class Smokescreen(Move):
    def __init__(self):
        super().__init__("Smokescreen", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Accuracy.
        """
        pass
