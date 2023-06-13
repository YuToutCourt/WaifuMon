from .move import Move
from waifu_types.type import Type

class DrumBeating(Move):
    def __init__(self):
        super().__init__("Drum Beating", type=Type.GRASS, power=80, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
