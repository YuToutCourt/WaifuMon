from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class JetPunch(Move):
    def __init__(self):
        super().__init__("Jet Punch", type=TypeFactory.create_type(Types.WATER), power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Always goes first.
        """
        pass
