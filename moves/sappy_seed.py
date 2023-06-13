from .move import Move
from waifu_types.type import Type

class SappySeed(Move):
    def __init__(self):
        super().__init__("Sappy Seed", type=Type.GRASS, power=90, accuracy=100, pp=15, proba_effect=100)

    def effect(self):
        """
        Drains HP from opponent each turn.
        """
        pass
