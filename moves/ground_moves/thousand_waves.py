from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ThousandWaves(Move):
    def __init__(self):
        super().__init__("Thousand Waves", type=TypeFactory.create_type(Types.GROUND), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Opponent cannot flee or switch.
        """
        pass
