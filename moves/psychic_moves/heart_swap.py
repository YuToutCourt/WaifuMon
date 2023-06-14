from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HeartSwap(Move):
    def __init__(self):
        super().__init__("Heart Swap", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Stat changes are swapped with the opponent.
        """
        pass
