from .move import Move
from waifu_types.type import Type

class LastRespects(Move):
    def __init__(self):
        super().__init__("Last Respects", type=Type.GHOST, power=50, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Damages increases the more party Pokémon have been defeated.
        """
        pass
