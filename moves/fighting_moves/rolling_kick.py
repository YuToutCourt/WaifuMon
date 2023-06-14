from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RollingKick(Move):
    def __init__(self):
        super().__init__("Rolling Kick", type=TypeFactory.create_type(Types.FIGHTING), power=60, accuracy=85, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
