from ..move import Move
from waifu_types.type import Type

class Overdrive(Move):
    def __init__(self):
        super().__init__("Overdrive", type=Type.ELECTRIC, power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
