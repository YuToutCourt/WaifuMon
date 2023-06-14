from ..move import Move
from waifu_types.type import Type

class ClangingScales(Move):
    def __init__(self):
        super().__init__("Clanging Scales", type=Type.DRAGON, power=110, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense.
        """
        pass
