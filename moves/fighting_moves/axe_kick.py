from ..move import Move
from waifu_types.type import Type

class AxeKick(Move):
    def __init__(self):
        super().__init__("Axe Kick", type=Type.FIGHTING, power=120, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        May confuse opponent. If it misses, the user loses HP.
        """
        pass
