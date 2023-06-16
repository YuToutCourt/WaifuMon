from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Sing(Move):
    def __init__(self):
        super().__init__("Sing", type=TypeFactory.create_type(Types.NORMAL), power=0, accuracy=55, pp=15, priority=0, proba_effect=100)

    def effect(self):
        """
        Puts opponent to sleep.
        """
        pass
