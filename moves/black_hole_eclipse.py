from .move import Move
from waifu_types.type import Type

class BlackHoleEclipse(Move):
    def __init__(self):
        super().__init__("Black Hole Eclipse", type=Type.DARK, power=0, accuracy=100, pp=1, proba_effect=100)

    def effect(self):
        """
        Dark type Z-Move.
        """
        pass
