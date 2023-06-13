from .move import Move
from waifu_types.type import Type

class Inferno(Move):
    def __init__(self):
        super().__init__("Inferno", type=Type.FIRE, power=100, accuracy=50, pp=5, proba_effect=100)

    def effect(self):
        """
        Burns opponent.
        """
        pass
