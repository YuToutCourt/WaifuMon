from .move import Move
from waifu_types.type import Type

class Extrasensory(Move):
    def __init__(self):
        super().__init__("Extrasensory", type=Type.PSYCHIC, power=80, accuracy=100, pp=20, proba_effect=10)

    def effect(self):
        """
        May cause flinching.
        """
        pass
