from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Soul-Stealing7-StarStrike(Move):
    def __init__(self):
        super().__init__("Soul-Stealing 7-Star Strike", type=TypeFactory.create_type(Types.GHOST), power=195, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Marshadow-exclusive Z-Move.
        """
        pass
