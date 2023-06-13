from .move import Move
from waifu_types.type import Type

class NastyPlot(Move):
    def __init__(self):
        super().__init__("Nasty Plot", type=Type.DARK, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Special Attack.
        """
        pass
