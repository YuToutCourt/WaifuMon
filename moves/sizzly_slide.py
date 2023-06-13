from .move import Move
from waifu_types.type import Type

class SizzlySlide(Move):
    def __init__(self):
        super().__init__("Sizzly Slide", type=Type.FIRE, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Burns the opponent.
        """
        pass
