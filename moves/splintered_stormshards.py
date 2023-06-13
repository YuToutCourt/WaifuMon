from .move import Move
from waifu_types.type import Type

class SplinteredStormshards(Move):
    def __init__(self):
        super().__init__("Splintered Stormshards", type=Type.ROCK, power=190, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Lycanroc-exclusive Z-Move.
        """
        pass
