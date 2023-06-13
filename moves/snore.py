from .move import Move
from waifu_types.type import Type

class Snore(Move):
    def __init__(self):
        super().__init__("Snore", type=Type.NORMAL, power=50, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        Can only be used if asleep. May cause flinching.
        """
        pass
