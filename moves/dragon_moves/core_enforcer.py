from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class CoreEnforcer(Move):
    def __init__(self):
        super().__init__("Core Enforcer", type=TypeFactory.create_type(Types.DRAGON), power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Suppresses the target's ability if the target has already moved.
        """
        pass
