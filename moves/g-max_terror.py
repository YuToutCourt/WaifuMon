from .move import Move
from waifu_types.type import Type

class G-MaxTerror(Move):
    def __init__(self):
        super().__init__("G-Max Terror", type=Type.GHOST, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Gengar-exclusive G-Max Move. Prevents opponent from switching out.
        """
        pass
