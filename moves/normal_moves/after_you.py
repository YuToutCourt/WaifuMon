from ..move import Move
from waifu_types.type import Type

class AfterYou(Move):
    def __init__(self):
        super().__init__("After You", type=Type.NORMAL, power=0, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Gives target priority in the next turn.
        """
        pass
