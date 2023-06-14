from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TripleArrows(Move):
    def __init__(self):
        super().__init__("Triple Arrows", type=TypeFactory.create_type(Types.FIGHTING), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises critical hit ratio and lowers target's Defense.
        """
        pass
