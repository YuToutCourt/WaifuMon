from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class OblivionWing(Move):
    def __init__(self):
        super().__init__("Oblivion Wing", type=TypeFactory.create_type(Types.FLYING), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User recovers most of the HP inflicted on opponent.
        """
        pass
