from moves.move import Move
from wtypes.type_factory import TypeFactory
from wtypes.enum_types import Types

class DoubleIronBash(Move):
    def __init__(self):
        super().__init__("Double Iron Bash", type=TypeFactory.create_type(Types.STEEL), power=60, accuracy=100, pp=5, priority=0, proba_effect=30)

    def effect(self):
        """
        Hits twice in one turn; may cause flinching.
        """
        pass
