from .move import Move
from waifu_types.type import Type

class HyperspaceHole(Move):
    def __init__(self):
        super().__init__("Hyperspace Hole", type=Type.PSYCHIC, power=80, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Can strike through Protect/Detect.
        """
        pass
