from .move import Move
from waifu_types.type import Type

class G-MaxCuddle(Move):
    def __init__(self):
        super().__init__("G-Max Cuddle", type=Type.NORMAL, power=0, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Eevee-exclusive G-Max Move. Infatuates opponents.
        """
        pass
