from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Trick-or-Treat(Move):
    def __init__(self):
        super().__init__("Trick-or-Treat", type=TypeFactory.create_type(Types.GHOST), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Adds Ghost type to opponent.
        """
        pass
