from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Judgment(Move):
    def __init__(self):
        super().__init__("Judgment", type=TypeFactory.create_type(Types.NORMAL), power=100, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Type depends on the Arceus Plate being held.
        """
        pass
