from .move import Move
from waifu_types.type import Type

class SpiderWeb(Move):
    def __init__(self):
        super().__init__("Spider Web", type=Type.BUG, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Opponent cannot escape/switch.
        """
        pass
