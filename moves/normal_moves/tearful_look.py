from ..move import Move
from waifu_types.type import Type

class TearfulLook(Move):
    def __init__(self):
        super().__init__("Tearful Look", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        The user gets teary eyed to make the target lose its combative spirit. This lowers the target's Attack and Sp. Atk stats.
        """
        pass
