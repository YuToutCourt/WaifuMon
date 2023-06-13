from .move import Move
from waifu_types.type import Type

class ShellSmash(Move):
    def __init__(self):
        super().__init__("Shell Smash", type=Type.NORMAL, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Attack, Special Attack and Speed but lowers Defense and Special Defense.
        """
        pass
