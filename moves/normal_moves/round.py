from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Round(Move):
    def __init__(self):
        super().__init__("Round", type=TypeFactory.create_type(Types.NORMAL), power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases if teammates use it in the same turn.
        """
        pass
