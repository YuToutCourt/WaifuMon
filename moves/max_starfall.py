from .move import Move
from waifu_types.type import Type

class MaxStarfall(Move):
    def __init__(self):
        super().__init__("Max Starfall", type=Type.FAIRY, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Fairy type Dynamax move. Summons Misty Terrain.
        """
        pass
