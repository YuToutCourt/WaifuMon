from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Double-Edge(Move):
    def __init__(self):
        super().__init__("Double-Edge", type=TypeFactory.create_type(Types.NORMAL), power=120, accuracy=100, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        User receives recoil damage.
        """
        pass
