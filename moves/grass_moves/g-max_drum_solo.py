from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxDrumSolo(Move):
    def __init__(self):
        super().__init__("G-Max Drum Solo", type=TypeFactory.create_type(Types.GRASS), power=160, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Rillaboom-exclusive G-Max Move. Ignores target's ability.
        """
        pass
