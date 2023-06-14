from ..move import Move
from waifu_types.type import Type

class RelicSong(Move):
    def __init__(self):
        super().__init__("Relic Song", type=Type.NORMAL, power=75, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May put the target to sleep.
        """
        pass
