from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DoubleHit(Move):
    def __init__(self):
        super().__init__("Double Hit", type=TypeFactory.create_type(Types.NORMAL), power=35, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
