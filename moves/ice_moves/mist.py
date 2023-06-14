from ..move import Move
from waifu_types.type import Type

class Mist(Move):
    def __init__(self):
        super().__init__("Mist", type=Type.ICE, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        User's stats cannot be changed for a period of time.
        """
        pass
