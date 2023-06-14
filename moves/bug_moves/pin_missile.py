from ..move import Move
from waifu_types.type import Type

class PinMissile(Move):
    def __init__(self):
        super().__init__("Pin Missile", type=Type.BUG, power=25, accuracy=95, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
