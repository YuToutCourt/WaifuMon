from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PsychoShift(Move):
    def __init__(self):
        super().__init__("Psycho Shift", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Transfers user's status condition to the opponent.
        """
        pass
