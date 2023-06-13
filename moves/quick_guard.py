from .move import Move
from waifu_types.type import Type

class QuickGuard(Move):
    def __init__(self):
        super().__init__("Quick Guard", type=Type.FIGHTING, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Protects the user's team from high-priority moves.
        """
        pass
