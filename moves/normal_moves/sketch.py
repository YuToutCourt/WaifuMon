from ..move import Move
from waifu_types.type import Type

class Sketch(Move):
    def __init__(self):
        super().__init__("Sketch", type=Type.NORMAL, power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Permanently copies the opponent's last move.
        """
        pass
