from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ZapCannon(Move):
    def __init__(self):
        super().__init__("Zap Cannon", type=TypeFactory.create_type(Types.ELECTRIC), power=120, accuracy=50, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        Paralyzes opponent.
        """
        pass
