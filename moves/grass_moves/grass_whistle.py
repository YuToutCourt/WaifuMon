from ..move import Move
from waifu_types.type import Type

class GrassWhistle(Move):
    def __init__(self):
        super().__init__("Grass Whistle", type=Type.GRASS, power=0, accuracy=55, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
