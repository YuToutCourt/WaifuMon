from .move import Move
from waifu_types.type import Type

class MaxDarkness(Move):
    def __init__(self):
        super().__init__("Max Darkness", type=Type.DARK, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Dark type Dynamax move. Lowers the target's Special Defense.
        """
        pass
