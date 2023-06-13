from .move import Move
from waifu_types.type import Type

class Glare(Move):
    def __init__(self):
        super().__init__("Glare", type=Type.NORMAL, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
