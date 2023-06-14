from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Camouflage(Move):
    def __init__(self):
        super().__init__("Camouflage", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Changes user's type according to the location.
        """
        pass
