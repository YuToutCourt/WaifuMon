from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DoubleShock(Move):
    def __init__(self):
        super().__init__("Double Shock", type=TypeFactory.create_type(Types.ELECTRIC), power=120, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        After using this move, the user will no longer be Electric type.
        """
        pass
