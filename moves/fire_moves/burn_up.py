from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class BurnUp(Move):
    def __init__(self):
        super().__init__("Burn Up", type=TypeFactory.create_type(Types.FIRE), power=130, accuracy=100, pp=5, priority=0, proba_effect=100)

    def effect(self):
        """
        To inflict massive damage, the user burns itself out. After using this move, the user will no longer be Fire type.
        """
        pass
