from ..move import Move
from waifu_types.type import Type

class Lock-On(Move):
    def __init__(self):
        super().__init__("Lock-On", type=Type.NORMAL, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User's next attack is guaranteed to hit.
        """
        pass
