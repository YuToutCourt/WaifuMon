from .move import Move
from waifu_types.type import Type

class Gust(Move):
    def __init__(self):
        super().__init__("Gust", type=Type.FLYING, power=40, accuracy=100, pp=35, proba_effect=100)

    def effect(self):
        """
        Hits Pokémon using Fly/Bounce/Sky Drop with double power.
        """
        pass
