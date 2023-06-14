from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HydroSteam(Move):
    def __init__(self):
        super().__init__("Hydro Steam", type=TypeFactory.create_type(Types.WATER), power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases in harsh sunlight.
        """
        pass
