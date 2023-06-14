from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class GuardSwap(Move):
    def __init__(self):
        super().__init__("Guard Swap", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User and opponent swap Defense and Special Defense.
        """
        pass
