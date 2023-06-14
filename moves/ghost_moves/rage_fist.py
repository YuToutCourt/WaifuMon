from ..move import Move
from waifu_types.type import Type

class RageFist(Move):
    def __init__(self):
        super().__init__("Rage Fist", type=Type.GHOST, power=50, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The more times the user has been hit by attacks, the greater the move's power.
        """
        pass
