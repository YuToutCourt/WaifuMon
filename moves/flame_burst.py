from .move import Move
from waifu_types.type import Type

class FlameBurst(Move):
    def __init__(self):
        super().__init__("Flame Burst", type=Type.FIRE, power=70, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        May also injure nearby Pokémon.
        """
        pass
