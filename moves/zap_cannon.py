from .move import Move
from waifu_types.type import Type

class ZapCannon(Move):
    def __init__(self):
        super().__init__("Zap Cannon", type=Type.ELECTRIC, power=120, accuracy=50, pp=5, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
