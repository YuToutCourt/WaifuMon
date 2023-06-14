from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxOvergrowth(Move):
    def __init__(self):
        super().__init__("Max Overgrowth", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Grass type Dynamax move. Summons Grassy Terrain.
        """
        pass
