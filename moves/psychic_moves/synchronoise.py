from ..move import Move
from waifu_types.type import Type

class Synchronoise(Move):
    def __init__(self):
        super().__init__("Synchronoise", type=Type.PSYCHIC, power=120, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits any Pokémon that shares a type with the user.
        """
        pass
