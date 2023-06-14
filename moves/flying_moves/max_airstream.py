from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxAirstream(Move):
    def __init__(self):
        super().__init__("Max Airstream", type=TypeFactory.create_type(Types.FLYING), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Flying type Dynamax move. Raises the team's Speed.
        """
        pass
