from .move import Move
from waifu_types.type import Type

class AirSlash(Move):
    def __init__(self):
        super().__init__("Air Slash", type=Type.FLYING, power=75, accuracy=95, pp=15, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
