from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PoisonTail(Move):
    def __init__(self):
        super().__init__("Poison Tail", type=TypeFactory.create_type(Types.POISON), power=50, accuracy=100, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        High critical hit ratio. May poison opponent.
        """
        pass
