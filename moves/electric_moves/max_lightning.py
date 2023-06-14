from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxLightning(Move):
    def __init__(self):
        super().__init__("Max Lightning", type=TypeFactory.create_type(Types.ELECTRIC), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Electric type Dynamax move. Summons Electric Terrain.
        """
        pass
