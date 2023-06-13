from .move import Move
from waifu_types.type import Type

class Scald(Move):
    def __init__(self):
        super().__init__("Scald", type=Type.WATER, power=80, accuracy=100, pp=15, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
