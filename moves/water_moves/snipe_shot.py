from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SnipeShot(Move):
    def __init__(self):
        super().__init__("Snipe Shot", type=TypeFactory.create_type(Types.WATER), power=80, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Ignores moves and abilities that draw in moves. High critical hit ratio.
        """
        pass
