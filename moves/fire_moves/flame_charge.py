from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FlameCharge(Move):
    def __init__(self):
        super().__init__("Flame Charge", type=TypeFactory.create_type(Types.FIRE), power=50, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Speed.
        """
        pass
