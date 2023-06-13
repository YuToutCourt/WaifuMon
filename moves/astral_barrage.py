from .move import Move
from waifu_types.type import Type

class AstralBarrage(Move):
    def __init__(self):
        super().__init__("Astral Barrage", type=Type.GHOST, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        The user attacks by sending a frightful amount of small ghosts at opposing Pokémon.
        """
        pass
