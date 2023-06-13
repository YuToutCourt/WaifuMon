from .move import Move
from waifu_types.type import Type

class G-MaxWildfire(Move):
    def __init__(self):
        super().__init__("G-Max Wildfire", type=Type.FIRE, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Charizard-exclusive G-Max Move. Damages non-Fire types for 4 turns.
        """
        pass
