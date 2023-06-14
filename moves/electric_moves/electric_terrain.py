from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ElectricTerrain(Move):
    def __init__(self):
        super().__init__("Electric Terrain", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Prevents all Pokémon from falling asleep for 5 turns.
        """
        pass
