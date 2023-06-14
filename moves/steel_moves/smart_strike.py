from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class SmartStrike(Move):
    def __init__(self):
        super().__init__("Smart Strike", type=TypeFactory.create_type(Types.STEEL), power=70, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user stabs the target with a sharp horn. This attack never misses.
        """
        pass
