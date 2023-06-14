from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxHailstorm(Move):
    def __init__(self):
        super().__init__("Max Hailstorm", type=TypeFactory.create_type(Types.ICE), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Ice type Dynamax move. Summons hail.
        """
        pass
