from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class LashOut(Move):
    def __init__(self):
        super().__init__("Lash Out", type=TypeFactory.create_type(Types.DARK), power=75, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Double power if stats were lowered during the turn.
        """
        pass
