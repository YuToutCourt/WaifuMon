from ..move import Move
from waifu_types.type import Type

class Swallow(Move):
    def __init__(self):
        super().__init__("Swallow", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The more times the user has performed Stockpile, the more HP is recovered.
        """
        pass
