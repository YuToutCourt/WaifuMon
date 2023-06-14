from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ChipAway(Move):
    def __init__(self):
        super().__init__("Chip Away", type=TypeFactory.create_type(Types.NORMAL), power=70, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores opponent's stat changes.
        """
        pass
