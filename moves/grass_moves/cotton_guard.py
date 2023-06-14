from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class CottonGuard(Move):
    def __init__(self):
        super().__init__("Cotton Guard", type=TypeFactory.create_type(Types.GRASS), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Drastically raises user's Defense.
        """
        pass
