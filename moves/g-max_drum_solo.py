from .move import Move
from waifu_types.type import Type

class G-MaxDrumSolo(Move):
    def __init__(self):
        super().__init__("G-Max Drum Solo", type=Type.GRASS, power=160, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Rillaboom-exclusive G-Max Move. Ignores target's ability.
        """
        pass
