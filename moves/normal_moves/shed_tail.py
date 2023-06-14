from ..move import Move
from waifu_types.type import Type

class ShedTail(Move):
    def __init__(self):
        super().__init__("Shed Tail", type=Type.NORMAL, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Creates a substitute, then swaps places with a party Pokémon in waiting.
        """
        pass
