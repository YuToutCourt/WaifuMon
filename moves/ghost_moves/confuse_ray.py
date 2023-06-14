from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ConfuseRay(Move):
    def __init__(self):
        super().__init__("Confuse Ray", type=TypeFactory.create_type(Types.GHOST), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Confuses opponent.
        """
        pass
