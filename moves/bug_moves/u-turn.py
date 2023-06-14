from ..move import Move
from waifu_types.type import Type

class U-turn(Move):
    def __init__(self):
        super().__init__("U-turn", type=Type.BUG, power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User switches out immediately after attacking.
        """
        pass
