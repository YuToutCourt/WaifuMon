from ..move import Move
from waifu_types.type import Type

class CometPunch(Move):
    def __init__(self):
        super().__init__("Comet Punch", type=Type.NORMAL, power=18, accuracy=85, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
