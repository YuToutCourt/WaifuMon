from .move import Move
from waifu_types.type import Type

class Return(Move):
    def __init__(self):
        super().__init__("Return", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Power increases with higher Friendship.
        """
        pass
