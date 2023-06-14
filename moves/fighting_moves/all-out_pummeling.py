from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class All-OutPummeling(Move):
    def __init__(self):
        super().__init__("All-Out Pummeling", type=TypeFactory.create_type(Types.FIGHTING), power=0, accuracy=100, pp=1, priority=0, proba_effect=100)

    def effect(self):
        """
        Fighting type Z-Move.
        """
        pass
