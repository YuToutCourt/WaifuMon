from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Ruination(Move):
    def __init__(self):
        super().__init__("Ruination", type=TypeFactory.create_type(Types.DARK), power=1, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Halves the opponent's HP.
        """
        pass
