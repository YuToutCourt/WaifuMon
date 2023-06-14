from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Earthquake(Move):
    def __init__(self):
        super().__init__("Earthquake", type=TypeFactory.create_type(Types.GROUND), power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power is doubled if opponent is underground from using Dig.
        """
        pass
