from .move import Move
from waifu_types.type import Type

class Topsy-Turvy(Move):
    def __init__(self):
        super().__init__("Topsy-Turvy", type=Type.DARK, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Reverses stat changes of opponent.
        """
        pass
