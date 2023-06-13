from .move import Move
from waifu_types.type import Type

class GlacialLance(Move):
    def __init__(self):
        super().__init__("Glacial Lance", type=Type.ICE, power=120, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        The user attacks by hurling a blizzard-cloaked icicle lance at opposing Pokémon.
        """
        pass
