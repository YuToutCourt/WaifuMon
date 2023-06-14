from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Protect(Move):
    def __init__(self):
        super().__init__("Protect", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Protects the user, but may fail if used consecutively.
        """
        pass
