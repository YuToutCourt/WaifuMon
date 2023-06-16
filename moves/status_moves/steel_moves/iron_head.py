from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IronHead(Move):
    def __init__(self):
        super().__init__("Iron Head", type=TypeFactory.create_type(Types.STEEL), power=80, accuracy=100, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
