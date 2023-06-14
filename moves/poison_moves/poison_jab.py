from ..move import Move
from waifu_types.type import Type

class PoisonJab(Move):
    def __init__(self):
        super().__init__("Poison Jab", type=Type.POISON, power=80, accuracy=100, pp=20, priority=0, proba_effect=30)

    def effect(self):
        """
        May poison the opponent.
        """
        pass
