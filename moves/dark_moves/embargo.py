from ..move import Move
from waifu_types.type import Type

class Embargo(Move):
    def __init__(self):
        super().__init__("Embargo", type=Type.DARK, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot use items.
        """
        pass
