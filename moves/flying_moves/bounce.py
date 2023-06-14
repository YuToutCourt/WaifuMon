from ..move import Move
from waifu_types.type import Type

class Bounce(Move):
    def __init__(self):
        super().__init__("Bounce", type=Type.FLYING, power=85, accuracy=85, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        Springs up on first turn, attacks on second. May paralyze opponent.
        """
        pass
