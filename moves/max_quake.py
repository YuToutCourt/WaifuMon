from .move import Move
from waifu_types.type import Type

class MaxQuake(Move):
    def __init__(self):
        super().__init__("Max Quake", type=Type.GROUND, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Ground type Dynamax move. Increases the team's Special Defense.
        """
        pass
