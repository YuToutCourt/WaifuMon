from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SteelWing(Move):
    def __init__(self):
        super().__init__("Steel Wing", type=TypeFactory.create_type(Types.STEEL), power=70, accuracy=90, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        May raise user's Defense.
        """
        pass
