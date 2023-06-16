from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IceFang(Move):
    def __init__(self):
        super().__init__("Ice Fang", type=TypeFactory.create_type(Types.ICE), power=65, accuracy=95, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May cause flinching and/or freeze opponent.
        """
        pass
