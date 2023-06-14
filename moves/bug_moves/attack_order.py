from ..move import Move
from waifu_types.type import Type

class AttackOrder(Move):
    def __init__(self):
        super().__init__("Attack Order", type=Type.BUG, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
