from ..move import Move
from waifu_types.type import Type

class BugBite(Move):
    def __init__(self):
        super().__init__("Bug Bite", type=Type.BUG, power=60, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Receives the effect from the opponent's held berry.
        """
        pass
