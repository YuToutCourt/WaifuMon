from ..move import Move
from waifu_types.type import Type

class ElectricTerrain(Move):
    def __init__(self):
        super().__init__("Electric Terrain", type=Type.ELECTRIC, power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents all Pokémon from falling asleep for 5 turns.
        """
        pass
