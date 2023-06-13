from .move import Move
from waifu_types.type import Type

class DreamEater(Move):
    def __init__(self):
        super().__init__("Dream Eater", type=Type.PSYCHIC, power=100, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        User recovers half the HP inflicted on a sleeping opponent.
        """
        pass
