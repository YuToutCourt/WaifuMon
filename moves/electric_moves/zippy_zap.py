from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ZippyZap(Move):
    def __init__(self):
        super().__init__("Zippy Zap", type=TypeFactory.create_type(Types.ELECTRIC), power=50, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Always results in a critical hit.
        """
        pass
