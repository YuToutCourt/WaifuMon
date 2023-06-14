from ..move import Move
from waifu_types.type import Type

class ShellTrap(Move):
    def __init__(self):
        super().__init__("Shell Trap", type=Type.FIRE, power=150, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals more damage to opponent if hit by a Physical move.
        """
        pass
