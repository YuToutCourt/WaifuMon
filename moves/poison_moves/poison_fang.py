from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PoisonFang(Move):
    def __init__(self):
        super().__init__("Poison Fang", type=TypeFactory.create_type(Types.POISON), power=50, accuracy=100, pp=15, priority=0, proba_effect=50)

    def effect(self):
        """
        May badly poison opponent.
        """
        pass
