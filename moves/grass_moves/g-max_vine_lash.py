from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxVineLash(Move):
    def __init__(self):
        super().__init__("G-Max Vine Lash", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Venusaur-exclusive G-Max Move. Damages non-Grass types for 4 turns.
        """
        pass
