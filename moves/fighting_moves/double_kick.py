from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DoubleKick(Move):
    def __init__(self):
        super().__init__("Double Kick", type=TypeFactory.create_type(Types.FIGHTING), power=30, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
