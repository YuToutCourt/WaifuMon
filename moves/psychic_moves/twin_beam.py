from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class TwinBeam(Move):
    def __init__(self):
        super().__init__("Twin Beam", type=TypeFactory.create_type(Types.PSYCHIC), power=40, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits twice in one turn.
        """
        pass
