from ..move import Move
from waifu_types.type import Type

class FairyLock(Move):
    def __init__(self):
        super().__init__("Fairy Lock", type=Type.FAIRY, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents fleeing in the next turn.
        """
        pass
