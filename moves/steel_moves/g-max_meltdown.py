from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxMeltdown(Move):
    def __init__(self):
        super().__init__("G-Max Meltdown", type=TypeFactory.create_type(Types.STEEL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Melmetal-exclusive G-Max Move. Prevents opponents using the same move twice in a row.
        """
        pass
