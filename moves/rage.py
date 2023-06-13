from .move import Move
from waifu_types.type import Type

class Rage(Move):
    def __init__(self):
        super().__init__("Rage", type=Type.NORMAL, power=20, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack when hit.
        """
        pass
