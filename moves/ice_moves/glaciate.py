from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Glaciate(Move):
    def __init__(self):
        super().__init__("Glaciate", type=TypeFactory.create_type(Types.ICE), power=65, accuracy=95, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Speed.
        """
        pass
