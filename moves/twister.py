from .move import Move
from waifu_types.type import Type

class Twister(Move):
    def __init__(self):
        super().__init__("Twister", type=Type.DRAGON, power=40, accuracy=100, pp=20, proba_effect=20)

    def effect(self):
        """
        May cause flinching. Hits Pokémon using Fly/Bounce with double power.
        """
        pass
