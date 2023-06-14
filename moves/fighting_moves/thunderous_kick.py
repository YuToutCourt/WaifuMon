from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class ThunderousKick(Move):
    def __init__(self):
        super().__init__("Thunderous Kick", type=TypeFactory.create_type(Types.FIGHTING), power=90, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Lowers opponent's Defense.
        """
        pass
