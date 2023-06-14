from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SteelBeam(Move):
    def __init__(self):
        super().__init__("Steel Beam", type=TypeFactory.create_type(Types.STEEL), power=140, accuracy=95, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User loses 50% of its HP.
        """
        pass
