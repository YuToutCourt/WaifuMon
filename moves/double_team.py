from .move import Move
from waifu_types.type import Type

class DoubleTeam(Move):
    def __init__(self):
        super().__init__("Double Team", type=Type.NORMAL, power=0, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Raises user's Evasiveness.
        """
        pass
