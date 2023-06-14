from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FusionFlare(Move):
    def __init__(self):
        super().__init__("Fusion Flare", type=TypeFactory.create_type(Types.FIRE), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases if Fusion Bolt is used in the same turn.
        """
        pass
