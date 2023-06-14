from ..move import Move
from waifu_types.type import Type

class DualWingbeat(Move):
    def __init__(self):
        super().__init__("Dual Wingbeat", type=Type.FLYING, power=40, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user slams the target with its wings. The target is hit twice in a row.
        """
        pass
