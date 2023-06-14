from ..move import Move
from waifu_types.type import Type

class WideGuard(Move):
    def __init__(self):
        super().__init__("Wide Guard", type=Type.ROCK, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user's team from multi-target attacks.
        """
        pass
