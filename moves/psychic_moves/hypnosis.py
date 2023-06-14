from ..move import Move
from waifu_types.type import Type

class Hypnosis(Move):
    def __init__(self):
        super().__init__("Hypnosis", type=Type.PSYCHIC, power=0, accuracy=60, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
