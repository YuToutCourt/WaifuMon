from .move import Move
from waifu_types.type import Type

class MaxRockfall(Move):
    def __init__(self):
        super().__init__("Max Rockfall", type=Type.ROCK, power=0, accuracy=100, pp=—, proba_effect=100)

    def effect(self):
        """
        Rock type Dynamax move. Summons a sandstorm.
        """
        pass
