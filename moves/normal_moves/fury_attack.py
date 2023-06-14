from ..move import Move
from waifu_types.type import Type

class FuryAttack(Move):
    def __init__(self):
        super().__init__("Fury Attack", type=Type.NORMAL, power=15, accuracy=85, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
