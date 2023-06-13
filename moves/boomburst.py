from .move import Move
from waifu_types.type import Type

class Boomburst(Move):
    def __init__(self):
        super().__init__("Boomburst", type=Type.NORMAL, power=140, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent Pokémon.
        """
        pass
