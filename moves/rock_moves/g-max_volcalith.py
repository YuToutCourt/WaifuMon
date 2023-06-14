from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxVolcalith(Move):
    def __init__(self):
        super().__init__("G-Max Volcalith", type=TypeFactory.create_type(Types.ROCK), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Coalossal-exclusive G-Max Move. Deals damage for 4 turns.
        """
        pass
