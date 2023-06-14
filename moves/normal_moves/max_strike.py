from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxStrike(Move):
    def __init__(self):
        super().__init__("Max Strike", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Normal type Dynamax move. Lowers the target's Speed.
        """
        pass
