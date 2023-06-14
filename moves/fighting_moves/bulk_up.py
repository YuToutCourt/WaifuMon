from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BulkUp(Move):
    def __init__(self):
        super().__init__("Bulk Up", type=TypeFactory.create_type(Types.FIGHTING), power=0, accuracy=100, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Attack and Defense.
        """
        pass
