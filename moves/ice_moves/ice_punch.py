from ..move import Move
from waifu_types.type import Type

class IcePunch(Move):
    def __init__(self):
        super().__init__("Ice Punch", type=Type.ICE, power=75, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
