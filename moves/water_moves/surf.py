from ..move import Move
from waifu_types.type import Type

class Surf(Move):
    def __init__(self):
        super().__init__("Surf", type=Type.WATER, power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent Pokémon.
        """
        pass
