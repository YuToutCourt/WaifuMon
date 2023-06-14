from ..move import Move
from waifu_types.type import Type

class GrassyTerrain(Move):
    def __init__(self):
        super().__init__("Grassy Terrain", type=Type.GRASS, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Restores a little HP of all Pokémon for 5 turns. 
        """
        pass
