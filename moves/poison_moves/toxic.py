from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Toxic(Move):
    def __init__(self):
        super().__init__("Toxic", type=TypeFactory.create_type(Types.POISON), power=0, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Badly poisons opponent.
        """
        pass
