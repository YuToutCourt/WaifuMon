from .move import Move
from waifu_types.type import Type

class Never-EndingNightmare(Move):
    def __init__(self):
        super().__init__("Never-Ending Nightmare", type=Type.GHOST, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Ghost type Z-Move.
        """
        pass
