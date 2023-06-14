from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SunsteelStrike(Move):
    def __init__(self):
        super().__init__("Sunsteel Strike", type=TypeFactory.create_type(Types.STEEL), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores the target's ability.
        """
        pass
