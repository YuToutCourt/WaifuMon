from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SignalBeam(Move):
    def __init__(self):
        super().__init__("Signal Beam", type=TypeFactory.create_type(Types.BUG), power=75, accuracy=100, pp=15, priority=0, proba_effect=10)

    def effect(self):
        """
        May confuse opponent.
        """
        pass
