from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class WildboltStorm(Move):
    def __init__(self):
        super().__init__("Wildbolt Storm", type=TypeFactory.create_type(Types.ELECTRIC), power=100, accuracy=80, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        May paralyze target.
        """
        pass
