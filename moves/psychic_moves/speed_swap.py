from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SpeedSwap(Move):
    def __init__(self):
        super().__init__("Speed Swap", type=TypeFactory.create_type(Types.PSYCHIC), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user exchanges Speed stats with the target.
        """
        pass
