from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Flamethrower(Move):
    def __init__(self):
        super().__init__("Flamethrower", type=TypeFactory.create_type(Types.FIRE), power=90, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
