from .move import Move
from waifu_types.type import Type

class Disable(Move):
    def __init__(self):
        super().__init__("Disable", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Opponent can't use its last attack for a few turns.
        """
        pass
