from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BlastBurn(Move):
    def __init__(self):
        super().__init__("Blast Burn", type=TypeFactory.create_type(Types.FIRE), power=150, accuracy=90, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        User must recharge next turn.
        """
        pass
