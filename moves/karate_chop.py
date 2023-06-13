from .move import Move
from waifu_types.type import Type

class KarateChop(Move):
    def __init__(self):
        super().__init__("Karate Chop", type=Type.FIGHTING, power=50, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
