from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FusionBolt(Move):
    def __init__(self):
        super().__init__("Fusion Bolt", type=TypeFactory.create_type(Types.ELECTRIC), power=100, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Power increases if Fusion Flare is used in the same turn.
        """
        pass
