from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ShellSideArm(Move):
    def __init__(self):
        super().__init__("Shell Side Arm", type=TypeFactory.create_type(Types.POISON), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        May poison opponent. Inflicts either Special or Physical damage, whichever is better.
        """
        pass
