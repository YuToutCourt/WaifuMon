from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class WaterPulse(Move):
    def __init__(self):
        super().__init__("Water Pulse", type=TypeFactory.create_type(Types.WATER), power=60, accuracy=100, pp=20, priority=0, proba_effect=20)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
