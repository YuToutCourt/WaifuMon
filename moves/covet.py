from .move import Move
from waifu_types.type import Type

class Covet(Move):
    def __init__(self):
        super().__init__("Covet", type=Type.NORMAL, power=60, accuracy=100, pp=25, proba_effect=100)

    def effect(self):
        """
        Opponent's item is stolen by the user.
        """
        pass
