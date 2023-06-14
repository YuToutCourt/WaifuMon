from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxFlare(Move):
    def __init__(self):
        super().__init__("Max Flare", type=TypeFactory.create_type(Types.FIRE), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Fire type Dynamax move. Summons harsh sunlight.
        """
        pass
