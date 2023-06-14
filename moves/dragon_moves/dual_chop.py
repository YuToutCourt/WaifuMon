from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DualChop(Move):
    def __init__(self):
        super().__init__("Dual Chop", type=TypeFactory.create_type(Types.DRAGON), power=40, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
