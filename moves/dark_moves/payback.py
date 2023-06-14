from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Payback(Move):
    def __init__(self):
        super().__init__("Payback", type=TypeFactory.create_type(Types.DARK), power=50, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Power doubles if the user was attacked first.
        """
        pass
