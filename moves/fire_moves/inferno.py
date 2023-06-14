from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Inferno(Move):
    def __init__(self):
        super().__init__("Inferno", type=TypeFactory.create_type(Types.FIRE), power=100, accuracy=50, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Burns opponent.
        """
        pass
