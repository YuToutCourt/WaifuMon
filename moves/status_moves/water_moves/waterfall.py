from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class Waterfall(Move):
    def __init__(self):
        super().__init__("Waterfall", type=TypeFactory.create_type(Types.WATER), power=80, accuracy=100, pp=15, priority=0, proba_effect=20)

    def effect(self):
        """
        May cause flinching.
        """
        pass
