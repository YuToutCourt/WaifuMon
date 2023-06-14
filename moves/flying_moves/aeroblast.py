from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Aeroblast(Move):
    def __init__(self):
        super().__init__("Aeroblast", type=TypeFactory.create_type(Types.FLYING), power=100, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
