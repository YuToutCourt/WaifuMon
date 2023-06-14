from ..move import Move
from waifu_types.type import Type

class Haze(Move):
    def __init__(self):
        super().__init__("Haze", type=Type.ICE, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Resets all stat changes.
        """
        pass
