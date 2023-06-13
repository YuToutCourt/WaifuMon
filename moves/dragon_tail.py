from .move import Move
from waifu_types.type import Type

class DragonTail(Move):
    def __init__(self):
        super().__init__("Dragon Tail", type=Type.DRAGON, power=60, accuracy=90, pp=10, proba_effect=100)

    def effect(self):
        """
        In battles, the opponent switches. In the wild, the Pokémon runs.
        """
        pass
