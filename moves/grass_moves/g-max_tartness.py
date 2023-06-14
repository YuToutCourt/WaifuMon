from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxTartness(Move):
    def __init__(self):
        super().__init__("G-Max Tartness", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Flapple-exclusive G-Max Move. Reduces opponents' evasiveness.
        """
        pass
