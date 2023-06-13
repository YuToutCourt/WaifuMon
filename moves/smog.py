from .move import Move
from waifu_types.type import Type

class Smog(Move):
    def __init__(self):
        super().__init__("Smog", type=Type.POISON, power=30, accuracy=70, pp=20, proba_effect=40)

    def effect(self):
        """
        May poison opponent.
        """
        pass
