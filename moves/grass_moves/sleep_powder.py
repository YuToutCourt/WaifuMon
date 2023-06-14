from ..move import Move
from waifu_types.type import Type

class SleepPowder(Move):
    def __init__(self):
        super().__init__("Sleep Powder", type=Type.GRASS, power=0, accuracy=75, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
