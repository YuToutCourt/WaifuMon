from .move import Move
from waifu_types.type import Type

class ThunderousKick(Move):
    def __init__(self):
        super().__init__("Thunderous Kick", type=Type.FIGHTING, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Defense.
        """
        pass
