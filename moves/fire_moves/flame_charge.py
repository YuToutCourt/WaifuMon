from ..move import Move
from waifu_types.type import Type

class FlameCharge(Move):
    def __init__(self):
        super().__init__("Flame Charge", type=Type.FIRE, power=50, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Speed.
        """
        pass
