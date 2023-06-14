from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TriAttack(Move):
    def __init__(self):
        super().__init__("Tri Attack", type=TypeFactory.create_type(Types.NORMAL), power=80, accuracy=100, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May paralyze, burn or freeze opponent.
        """
        pass
