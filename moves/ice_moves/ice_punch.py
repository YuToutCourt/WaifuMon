from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IcePunch(Move):
    def __init__(self):
        super().__init__("Ice Punch", type=TypeFactory.create_type(Types.ICE), power=75, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
