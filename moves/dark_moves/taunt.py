from ..move import Move
from waifu_types.type import Type

class Taunt(Move):
    def __init__(self):
        super().__init__("Taunt", type=Type.DARK, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent can only use moves that attack.
        """
        pass
