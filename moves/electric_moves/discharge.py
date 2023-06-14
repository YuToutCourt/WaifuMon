from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Discharge(Move):
    def __init__(self):
        super().__init__("Discharge", type=TypeFactory.create_type(Types.ELECTRIC), power=80, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May paralyze opponent.
        """
        pass
