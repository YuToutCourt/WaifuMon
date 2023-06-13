from .move import Move
from waifu_types.type import Type

class ThousandWaves(Move):
    def __init__(self):
        super().__init__("Thousand Waves", type=Type.GROUND, power=90, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Opponent cannot flee or switch.
        """
        pass
