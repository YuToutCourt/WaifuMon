from .move import Move
from waifu_types.type import Type

class PsychicTerrain(Move):
    def __init__(self):
        super().__init__("Psychic Terrain", type=Type.PSYCHIC, power=0, accuracy=100, pp=10, proba_effect=100)

    def effect(self):
        """
        Prevents priority moves from being used for 5 turns.
        """
        pass
