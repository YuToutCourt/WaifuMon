from .move import Move
from waifu_types.type import Type

class Amnesia(Move):
    def __init__(self):
        super().__init__("Amnesia", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Special Defense.
        """
        pass
