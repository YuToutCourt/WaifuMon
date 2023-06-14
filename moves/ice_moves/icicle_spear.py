from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IcicleSpear(Move):
    def __init__(self):
        super().__init__("Icicle Spear", type=TypeFactory.create_type(Types.ICE), power=25, accuracy=100, pp=30, priority=0, proba_effect=100)

    def effect(self):
        """
        Hits 2-5 times in one turn.
        """
        pass
