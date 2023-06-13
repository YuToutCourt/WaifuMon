from .move import Move
from waifu_types.type import Type

class Teleport(Move):
    def __init__(self):
        super().__init__("Teleport", type=Type.PSYCHIC, power=0, accuracy=100, pp=20, proba_effect=100)

    def effect(self):
        """
        Allows user to flee wild battles; also warps player to last PokéCenter.
        """
        pass
