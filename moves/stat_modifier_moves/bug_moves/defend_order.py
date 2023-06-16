from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DefendOrder(Move):
    def __init__(self):
        super().__init__("Defend Order", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=10, priority=0, proba_effect=100)

    def effect(self):
        """
        Raises user's Defense and Special Defense.
        """
        pass
