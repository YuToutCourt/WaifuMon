from ..move import Move
from waifu_types.type import Type

class SunsteelStrike(Move):
    def __init__(self):
        super().__init__("Sunsteel Strike", type=Type.STEEL, power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores the target's ability.
        """
        pass
