from ..move import Move
from waifu_types.type import Type

class RagePowder(Move):
    def __init__(self):
        super().__init__("Rage Powder", type=Type.BUG, power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Forces attacks to hit user, not team-mates.
        """
        pass
