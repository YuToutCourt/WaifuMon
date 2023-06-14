from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DualWingbeat(Move):
    def __init__(self):
        super().__init__("Dual Wingbeat", type=TypeFactory.create_type(Types.FLYING), power=40, accuracy=90, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        The user slams the target with its wings. The target is hit twice in a row.
        """
        pass
