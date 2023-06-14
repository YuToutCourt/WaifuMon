from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxCentiferno(Move):
    def __init__(self):
        super().__init__("G-Max Centiferno", type=TypeFactory.create_type(Types.FIRE), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Centiskorch-exclusive G-Max Move. Traps opponents for 4-5 turns.
        """
        pass
