from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Screech(Move):
    def __init__(self):
        super().__init__("Screech", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=85, pp=40, priority=0, proba_effect=100)

    def effect(self):
        """
        Sharply lowers opponent's Defense.
        """
        pass
