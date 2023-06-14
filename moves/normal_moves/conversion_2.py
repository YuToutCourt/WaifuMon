from ..move import Move
from waifu_types.type import Type

class Conversion2(Move):
    def __init__(self):
        super().__init__("Conversion 2", type=Type.NORMAL, power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        User changes type to become resistant to opponent's last move.
        """
        pass
