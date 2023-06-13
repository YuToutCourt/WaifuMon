from .move import Move
from waifu_types.type import Type

class SpringtideStorm(Move):
    def __init__(self):
        super().__init__("Springtide Storm", type=Type.FAIRY, power=100, accuracy=80, pp=5, proba_effect=100)

    def effect(self):
        """
        Boosts user's stats in Incarnate Forme, or lowers opponent's stats in Therian Forme.
        """
        pass
