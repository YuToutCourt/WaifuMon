from .move import Move
from waifu_types.type import Type

class Roar(Move):
    def __init__(self):
        super().__init__("Roar", type=Type.NORMAL, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        In battles, the opponent switches. In the wild, the Pokémon runs.
        """
        pass
