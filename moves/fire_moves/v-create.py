from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class V-create(Move):
    def __init__(self):
        super().__init__("V-create", type=TypeFactory.create_type(Types.FIRE), power=180, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers user's Defense, Special Defense and Speed.
        """
        pass
