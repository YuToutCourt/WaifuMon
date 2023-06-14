from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MeanLook(Move):
    def __init__(self):
        super().__init__("Mean Look", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot flee or switch.
        """
        pass
