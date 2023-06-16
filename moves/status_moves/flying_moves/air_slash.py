from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AirSlash(Move):
    def __init__(self):
        super().__init__("Air Slash", type=TypeFactory.create_type(Types.FLYING), power=75, accuracy=95, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
