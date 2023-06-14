from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class PowderSnow(Move):
    def __init__(self):
        super().__init__("Powder Snow", type=TypeFactory.create_type(Types.ICE), power=40, accuracy=100, pp=25, priority=0, proba_effect=10)

    def effect(self):
        """
        May freeze opponent.
        """
        pass
