from ..move import Move
from waifu_types.type import Type

class MaxGuard(Move):
    def __init__(self):
        super().__init__("Max Guard", type=Type.NORMAL, power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Status category Dynamax move. Protects the user.
        """
        pass
