from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SearingShot(Move):
    def __init__(self):
        super().__init__("Searing Shot", type=TypeFactory.create_type(Types.FIRE), power=100, accuracy=100, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        May burn opponent.
        """
        pass
