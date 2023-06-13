from .move import Move
from waifu_types.type import Type

class SludgeWave(Move):
    def __init__(self):
        super().__init__("Sludge Wave", type=Type.POISON, power=95, accuracy=100, pp=10, proba_effect=10)

    def effect(self):
        """
        May poison opponent.
        """
        pass
