from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IronTail(Move):
    def __init__(self):
        super().__init__("Iron Tail", type=TypeFactory.create_type(Types.STEEL), power=100, accuracy=75, pp=15, priority=0, proba_effect=30)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
