from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Belch(Move):
    def __init__(self):
        super().__init__("Belch", type=TypeFactory.create_type(Types.POISON), power=120, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        User must have consumed a Berry.
        """
        pass
