from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Chloroblast(Move):
    def __init__(self):
        super().__init__("Chloroblast", type=TypeFactory.create_type(Types.GRASS), power=150, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
