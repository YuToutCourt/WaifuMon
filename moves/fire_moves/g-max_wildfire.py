from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxWildfire(Move):
    def __init__(self):
        super().__init__("G-Max Wildfire", type=TypeFactory.create_type(Types.FIRE), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Charizard-exclusive G-Max Move. Damages non-Fire types for 4 turns.
        """
        pass
