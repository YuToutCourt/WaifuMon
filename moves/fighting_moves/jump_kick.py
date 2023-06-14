from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class JumpKick(Move):
    def __init__(self):
        super().__init__("Jump Kick", type=TypeFactory.create_type(Types.FIGHTING), power=100, accuracy=95, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        If it misses, the user loses half their HP.
        """
        pass
