from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxTerror(Move):
    def __init__(self):
        super().__init__("G-Max Terror", type=TypeFactory.create_type(Types.GHOST), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Gengar-exclusive G-Max Move. Prevents opponent from switching out.
        """
        pass
