from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FreezyFrost(Move):
    def __init__(self):
        super().__init__("Freezy Frost", type=TypeFactory.create_type(Types.ICE), power=90, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Resets all stat changes.
        """
        pass
