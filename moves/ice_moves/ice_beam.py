from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IceBeam(Move):
    def __init__(self):
        super().__init__("Ice Beam", type=TypeFactory.create_type(Types.ICE), power=90, accuracy=100, pp=10, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
