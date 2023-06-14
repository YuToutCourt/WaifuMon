from ..move import Move
from waifu_types.type import Type

class Grudge(Move):
    def __init__(self):
        super().__init__("Grudge", type=Type.GHOST, power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        If the users faints after using this move, the PP for the opponent's last move is depleted.
        """
        pass
