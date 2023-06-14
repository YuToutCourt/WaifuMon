from ..move import Move
from waifu_types.type import Type

class Lunge(Move):
    def __init__(self):
        super().__init__("Lunge", type=Type.BUG, power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        The user makes a lunge at the target, attacking with full force. This also lowers the target's Attack stat.
        """
        pass
