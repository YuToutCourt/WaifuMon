from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SludgeWave(Move):
    def __init__(self):
        super().__init__("Sludge Wave", type=TypeFactory.create_type(Types.POISON), power=95, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May poison opponent.
        """
        pass
