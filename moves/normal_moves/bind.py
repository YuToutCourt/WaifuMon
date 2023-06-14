from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Bind(Move):
    def __init__(self):
        super().__init__("Bind", type=TypeFactory.create_type(Types.NORMAL), power=15, accuracy=85, pp=20, priority=0, proba_effect=100)

    def effect(self):
        """
        Traps opponent, damaging them for 4-5 turns.
        """
        pass
