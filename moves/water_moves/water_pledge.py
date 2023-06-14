from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class WaterPledge(Move):
    def __init__(self):
        super().__init__("Water Pledge", type=TypeFactory.create_type(Types.WATER), power=80, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Added effects appear if preceded by Fire Pledge or succeeded by Grass Pledge.
        """
        pass
