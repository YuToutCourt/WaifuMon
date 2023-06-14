from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class FurySwipes(Move):
    def __init__(self):
        super().__init__("Fury Swipes", type=TypeFactory.create_type(Types.NORMAL), power=18, accuracy=80, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
