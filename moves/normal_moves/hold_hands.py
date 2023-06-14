from ..move import Move
from waifu_types.type import Type

class HoldHands(Move):
    def __init__(self):
        super().__init__("Hold Hands", type=Type.NORMAL, power=0, accuracy=100, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Makes the user and an ally very happy.
        """
        pass
