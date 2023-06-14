from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MetalBurst(Move):
    def __init__(self):
        super().__init__("Metal Burst", type=TypeFactory.create_type(Types.STEEL), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Deals damage equal to 1.5x opponent's attack.
        """
        pass
