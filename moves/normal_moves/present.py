from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Present(Move):
    def __init__(self):
        super().__init__("Present", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=90, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Either deals damage or heals.
        """
        pass
