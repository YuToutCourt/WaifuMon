from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ChargeBeam(Move):
    def __init__(self):
        super().__init__("Charge Beam", type=TypeFactory.create_type(Types.ELECTRIC), power=50, accuracy=90, pp=10, priority=0, proba_effect=70)

    def effect(self):
        """
        May raise user's Special Attack.
        """
        pass
