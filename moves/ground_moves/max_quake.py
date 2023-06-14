from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxQuake(Move):
    def __init__(self):
        super().__init__("Max Quake", type=TypeFactory.create_type(Types.GROUND), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Ground type Dynamax move. Increases the team's Special Defense.
        """
        pass
