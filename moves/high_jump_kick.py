from .move import Move
from waifu_types.type import Type

class HighJumpKick(Move):
    def __init__(self):
        super().__init__("High Jump Kick", type=Type.FIGHTING, power=130, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        If it misses, the user loses half their HP.
        """
        pass
