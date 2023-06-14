from ..move import Move
from waifu_types.type import Type

class Copycat(Move):
    def __init__(self):
        super().__init__("Copycat", type=Type.NORMAL, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Copies opponent's last move.
        """
        pass
