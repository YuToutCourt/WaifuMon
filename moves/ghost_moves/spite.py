from ..move import Move
from waifu_types.type import Type

class Spite(Move):
    def __init__(self):
        super().__init__("Spite", type=Type.GHOST, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The opponent's last move loses 2-5 PP.
        """
        pass
