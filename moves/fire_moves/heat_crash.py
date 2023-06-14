from ..move import Move
from waifu_types.type import Type

class HeatCrash(Move):
    def __init__(self):
        super().__init__("Heat Crash", type=Type.FIRE, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The heavier the user, the stronger the attack.
        """
        pass
