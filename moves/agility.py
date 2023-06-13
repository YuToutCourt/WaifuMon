from .move import Move
from waifu_types.type import Type

class Agility(Move):
    def __init__(self):
        super().__init__("Agility", type=Type.PSYCHIC, power=0, accuracy=100, pp=30, proba_effect=100)

    def effect(self):
        """
        Sharply raises user's Speed.
        """
        pass
