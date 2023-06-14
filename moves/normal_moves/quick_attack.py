from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class QuickAttack(Move):
    def __init__(self):
        super().__init__("Quick Attack", type=TypeFactory.create_type(Types.NORMAL), power=40, accuracy=100, pp=30, priority=1, proba_effect=100)

    def effect(self):
        """
        User attacks first.
        """
        pass
