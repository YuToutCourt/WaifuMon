from .move import Move
from waifu_types.type import Type

class BoltBeak(Move):
    def __init__(self):
        super().__init__("Bolt Beak", type=Type.ELECTRIC, power=85, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        If the user attacks before the target, the power of this move is doubled.
        """
        pass
