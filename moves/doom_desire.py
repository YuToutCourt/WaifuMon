from .move import Move
from waifu_types.type import Type

class DoomDesire(Move):
    def __init__(self):
        super().__init__("Doom Desire", type=Type.STEEL, power=140, accuracy=100, pp=5, proba_effect=100)

    def effect(self):
        """
        Damage occurs 2 turns later.
        """
        pass
