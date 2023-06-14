from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class AirCutter(Move):
    def __init__(self):
        super().__init__("Air Cutter", type=TypeFactory.create_type(Types.FLYING), power=60, accuracy=95, pp=25, priority=0, proba_effect=100)

    def effect(self):
        """
        High critical hit ratio.
        """
        pass
