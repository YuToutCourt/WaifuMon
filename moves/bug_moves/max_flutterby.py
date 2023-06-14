from ..move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class MaxFlutterby(Move):
    def __init__(self):
        super().__init__("Max Flutterby", type=TypeFactory.create_type(Types.BUG), power=0, accuracy=100, pp=—, priority=0, proba_effect=100)

    def effect(self):
        """
        Bug type Dynamax move. Lowers the target's Special Attack.
        """
        pass
