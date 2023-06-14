from ..move import Move
from waifu_types.type import Type

class BreakingSwipe(Move):
    def __init__(self):
        super().__init__("Breaking Swipe", type=Type.DRAGON, power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits multiple opponents and lowers their attack.
        """
        pass
