from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Overdrive(Move):
    def __init__(self):
        super().__init__("Overdrive", type=TypeFactory.create_type(Types.ELECTRIC), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits all adjacent opponents.
        """
        pass
