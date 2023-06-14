from ..move import Move
from waifu_types.type import Type

class HealOrder(Move):
    def __init__(self):
        super().__init__("Heal Order", type=Type.BUG, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers half its max HP.
        """
        pass
