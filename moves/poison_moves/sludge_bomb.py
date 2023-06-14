from ..move import Move
from waifu_types.type import Type

class SludgeBomb(Move):
    def __init__(self):
        super().__init__("Sludge Bomb", type=Type.POISON, power=90, accuracy=100, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May poison opponent.
        """
        pass
