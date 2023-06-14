from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class HiddenPower(Move):
    def __init__(self):
        super().__init__("Hidden Power", type=TypeFactory.create_type(Types.NORMAL), power=60, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Type and power depends on user's IVs.
        """
        pass
