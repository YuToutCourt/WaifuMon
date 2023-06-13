from .move import Move
from waifu_types.type import Type

class Coaching(Move):
    def __init__(self):
        super().__init__("Coaching", type=Type.FIGHTING, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Boosts Attack and Defense of a teammate.
        """
        pass
