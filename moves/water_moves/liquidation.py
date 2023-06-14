from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Liquidation(Move):
    def __init__(self):
        super().__init__("Liquidation", type=TypeFactory.create_type(Types.WATER), power=85, accuracy=100, pp=10, priority=0, proba_effect=20)

    def effect(self):
        """
        May lower opponent's Defense.
        """
        pass
