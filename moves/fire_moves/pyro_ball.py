from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PyroBall(Move):
    def __init__(self):
        super().__init__("Pyro Ball", type=TypeFactory.create_type(Types.FIRE), power=120, accuracy=90, pp=5, priority=0, proba_effect=10)

    def effect(self):
        """
        May burn opponent.
        """
        pass
