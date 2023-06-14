from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Hail(Move):
    def __init__(self):
        super().__init__("Hail", type=TypeFactory.create_type(Types.ICE), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Non-Ice types are damaged for 5 turns.
        """
        pass
