from .move import Move
from waifu_types.type import Type

class Catastropika(Move):
    def __init__(self):
        super().__init__("Catastropika", type=Type.ELECTRIC, power=210, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Pikachu-exclusive Z-Move.
        """
        pass
