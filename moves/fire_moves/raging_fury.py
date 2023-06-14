from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class RagingFury(Move):
    def __init__(self):
        super().__init__("Raging Fury", type=TypeFactory.create_type(Types.FIRE), power=120, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User keeps repeating the same move over and over.
        """
        pass
