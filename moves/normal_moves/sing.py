from ..move import Move
from waifu_types.type import Type

class Sing(Move):
    def __init__(self):
        super().__init__("Sing", type=Type.NORMAL, power=0, accuracy=55, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
