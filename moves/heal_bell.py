from .move import Move
from waifu_types.type import Type

class HealBell(Move):
    def __init__(self):
        super().__init__("Heal Bell", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Heals the user's party's status conditions.
        """
        pass
