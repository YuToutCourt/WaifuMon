from .move import Move
from waifu_types.type import Type

class Minimize(Move):
    def __init__(self):
        super().__init__("Minimize", type=Type.NORMAL, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Evasiveness.
        """
        pass
