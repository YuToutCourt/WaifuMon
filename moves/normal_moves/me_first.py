from ..move import Move
from waifu_types.type import Type

class MeFirst(Move):
    def __init__(self):
        super().__init__("Me First", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        User copies the opponent's attack with 1.5× power.
        """
        pass
