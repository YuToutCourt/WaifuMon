from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class IcicleCrash(Move):
    def __init__(self):
        super().__init__("Icicle Crash", type=TypeFactory.create_type(Types.ICE), power=85, accuracy=90, pp=10, priority=0, proba_effect=30)

    def effect(self):
        """
        May cause flinching.
        """
        pass
