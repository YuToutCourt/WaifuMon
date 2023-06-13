from .move import Move
from waifu_types.type import Type

class Powder(Move):
    def __init__(self):
        super().__init__("Powder", type=Type.BUG, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Damages Pokémon using Fire type moves.
        """
        pass
