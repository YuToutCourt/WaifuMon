from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class OriginPulse(Move):
    def __init__(self):
        super().__init__("Origin Pulse", type=TypeFactory.create_type(Types.WATER), power=110, accuracy=85, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
