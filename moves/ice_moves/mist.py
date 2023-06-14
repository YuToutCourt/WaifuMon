from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Mist(Move):
    def __init__(self):
        super().__init__("Mist", type=TypeFactory.create_type(Types.ICE), power=0, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        User's stats cannot be changed for a period of time.
        """
        pass
