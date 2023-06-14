from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Struggle(Move):
    def __init__(self):
        super().__init__("Struggle", type=TypeFactory.create_type(Types.NORMAL), power=50, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Only usable when all PP are gone. Hurts the user.
        """
        pass
