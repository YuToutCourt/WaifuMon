from ..move import Move
from waifu_types.type import Type

class MaxMindstorm(Move):
    def __init__(self):
        super().__init__("Max Mindstorm", type=Type.PSYCHIC, power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Psychic type Dynamax move. Summons Psychic Terrain.
        """
        pass
