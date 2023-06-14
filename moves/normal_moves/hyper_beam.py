from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HyperBeam(Move):
    def __init__(self):
        super().__init__("Hyper Beam", type=TypeFactory.create_type(Types.NORMAL), power=150, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass
