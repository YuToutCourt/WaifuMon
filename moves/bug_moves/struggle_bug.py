from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class StruggleBug(Move):
    def __init__(self):
        super().__init__("Struggle Bug", type=TypeFactory.create_type(Types.BUG), power=50, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Special Attack.
        """
        pass
