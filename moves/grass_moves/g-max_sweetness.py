from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class G-MaxSweetness(Move):
    def __init__(self):
        super().__init__("G-Max Sweetness", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Appletun-exclusive G-Max Move. Heals status conditions of user's team.
        """
        pass
