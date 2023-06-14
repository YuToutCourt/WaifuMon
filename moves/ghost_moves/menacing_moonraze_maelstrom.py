from ..move import Move
from waifu_types.type import Type

class MenacingMoonrazeMaelstrom(Move):
    def __init__(self):
        super().__init__("Menacing Moonraze Maelstrom", type=Type.GHOST, power=200, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Lunala-exclusive Z-Move.
        """
        pass
