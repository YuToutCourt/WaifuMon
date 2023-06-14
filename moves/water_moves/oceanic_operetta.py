from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class OceanicOperetta(Move):
    def __init__(self):
        super().__init__("Oceanic Operetta", type=TypeFactory.create_type(Types.WATER), power=195, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Primarina-exclusive Z-Move.
        """
        pass
