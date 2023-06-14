from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxStarfall(Move):
    def __init__(self):
        super().__init__("Max Starfall", type=TypeFactory.create_type(Types.FAIRY), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Fairy type Dynamax move. Summons Misty Terrain.
        """
        pass
