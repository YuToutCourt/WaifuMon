from ..move import Move
from waifu_types.type import Type

class PoisonTail(Move):
    def __init__(self):
        super().__init__("Poison Tail", type=Type.POISON, power=50, accuracy=100, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        High critical hit ratio. May poison opponent.
        """
        pass
