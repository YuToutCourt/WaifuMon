from .move import Move
from waifu_types.type import Type

class MaxWyrmwind(Move):
    def __init__(self):
        super().__init__("Max Wyrmwind", type=Type.DRAGON, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Dragon type Dynamax move. Lowers the target's Attack.
        """
        pass
