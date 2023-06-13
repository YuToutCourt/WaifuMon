from .move import Move
from waifu_types.type import Type

class TropKick(Move):
    def __init__(self):
        super().__init__("Trop Kick", type=Type.GRASS, power=70, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Attack.
        """
        pass
