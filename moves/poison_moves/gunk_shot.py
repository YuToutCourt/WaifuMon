from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GunkShot(Move):
    def __init__(self):
        super().__init__("Gunk Shot", type=TypeFactory.create_type(Types.POISON), power=120, accuracy=80, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        May poison opponent.
        """
        pass
