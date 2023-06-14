from ..move import Move
from waifu_types.type import Type

class WonderRoom(Move):
    def __init__(self):
        super().__init__("Wonder Room", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Swaps every Pokémon's Defense and Special Defense for 5 turns.
        """
        pass
